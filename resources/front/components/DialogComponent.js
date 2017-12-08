import Vue from 'vue';
import $ from 'jquery';
import _ from 'lodash';
import Materialize from 'materialize-css';
import Storage from '../mixins/StorageMixin';
import Helper from '../mixins/HelperMixin';
import template from '../../tmp/components/dialog.html';

const Dialog = Vue.extend({
    template,
    props: ['user-role'],
    mixins: [Storage, Helper],
    data() {
        return {
            rightClass: 'right',
            leftClass: 'left',
            message: "",
            username: "",
            getter: null,
            isSelected: false,
            historyMessages: [],
            users: [{ unread: [], username: "" }],
            openedDialog: { messages: [], open: false, dialog_id: 0, username: '', unread: [] },
            dialogs: [],
            dialogId: 0,
        }
    },
    mounted() {
        this.init()
    },
    methods: {
        init() {
            $('select').material_select();
            $('#dialog_window').modal();
            this.triggerGetUsers();
            this.getUserDialogs();
            this.username = document.getElementById('username').innerText;
        },
        openDialog() {
            $('#dialog_window').modal('open');
        },
        getOffset(){
            console.log(this.openedDialog.messages.length)
            let self = this,
                limit = 20,
                offset = Math.floor(self.openedDialog.messages.length/limit);
            return offset;
        },
        getHistory(openedDialog) {
            let self = this,
                session = self.getSess(),
                offset = self.getOffset(),
                dialogId = self.openedDialog.dialog_id,
                uri = `/api/1/messages/history/${dialogId}/${session}/${offset}`;
                console.log(offset)
            $.get(uri).done(data => {
                if (data.error) {
                    return console.error(data.error)
                }
                if (data.length > 0) {
                    self.setHistoryToUser(data, dialogId)
                }
            })
            .fail(error => {
                console.error(error)
            })
        },
        setHistoryToUser(messages, dialogId){ 
            let messagesAll = this.openedDialog.messages;
            this.users.map(user => {
                if (user.dialog_id === dialogId) {
                    console.log(user.dialog_id)
                    _.each(messages, message => {
                        user.messages.push(message)
                        messagesAll.push(message)
                    })
                }
            });
            this.openedDialog = Object.assign({}, this.openDialog, {messages: messagesAll, open:true, dialog_id: dialogId, unread: []} )
        },
        getUserDialogs() {
            let self = this,
                session = self.getSess(),
                uri = `/api/1/messages/dialogs/${session}`;
            $.get(uri).done(data => {
                if (data.error) {
                    return console.error(data.error)
                }
                self.dialogs = data;
                _.each(self.users, item => {
                    self.setDialogsToUsers(item)
                })
            }).fail(error => {
                console.error(error)
            })
        },
        setDialogsToUsers(user) {
            let self = this,
                countUnread = 0,
                dialogs = [];
            dialogs = self.dialogs.filter(item => {
                if (self.username !== user.username) {
                    return item.from_user === user.username || item.to_user === user.username;
                } else {
                    return item.to_user === item.from_user && item.to_user === user.username;
                }
            })
            dialogs = _.uniqBy(dialogs, 'created_at')
            self.users.map(item => {
                if (item.username === user.username) {
                    let curUser = item.username;
                    item.messages = dialogs; item.open = false;
                    item.unread = item.messages.length > 0 ? self.dialogs.filter(item => {
                        return !item.read && self.username === item.to_user && item.to_user !== item.from_user && curUser === item.from_user
                    }) : [];
                    item.dialog_id = item.messages.length === 0 ? 0 : item.messages[0].dialog_id
                    console.log(item.unread)
                    if (self.username === user.username && item.username === self.username) {
                        item.unread = item.messages.length > 0 ? self.dialogs.filter(item => !item.read && self.username === item.to_user && item.to_user === item.from_user) : [];
                    }
                    item.unread = _.uniqBy(item.unread, 'created_at')
                }
                if (item.unread.length > 0)++countUnread;
            })
            if (countUnread > 0) self.$emit('transport-count', countUnread);
        },
        openUserDialog(user) {
            this.users.map(item => {
                item.open = false;
                if (item.username === user.username) {
                    if (item.unread.length > 0) this.readMessages(user)
                    item.open = true;
                    this.openedDialog = item;
                    this.isSelected = true;
                    this.getter = user.username;
                    this.dialogId = item.dialog_id;
                }
            });
        },
        readMessages(user) {
            console.log(user)
            let self = this,
                countUnread = 0,
                uri = '/api/1/messages/read/',
                session = self.getSess(),
                params = {
                    dialog: user.dialog_id,
                    sessionid: session
                };

            $.post(uri, params).done(data => {
                if (data.success) {
                    self.users.map(item => {
                        if (item.username === user.username) item.unread = [];
                        if (item.unread.length > 0)++countUnread;
                    })
                    self.$emit('transport-count', countUnread)
                }
                if (data.error) {
                    return console.error(data.error)
                }
            }).fail(error => {
                console.error(error)
            })
        },
        triggerGetUsers() {
            this.users = this.storageGet('users') !== null ? this.storageGet('users') : false;
            if (!this.users) this.getUsers();
        },
        getUsers() {
            let self = this,
                session = self.getSess(),
                uri = `/api/1/users/${session}`;
            $.get(uri)
                .done(data => {
                    if (data.error) {
                        return console.error(data.error)
                    }
                    self.users = data;
                })
                .fail(error => {
                    console.error(error);
                });
        },
        selectGetter(name) {
            document.querySelectorAll(".__dialog-field .materialize-textarea")[0].focus();
        },
        search(event) {
            let self = this,
                keyword = event.target.value,
                users = self.storageGet('users');
            if (keyword.length <= 2) return self.users = self.storageGet('users');;
            self.users = users.filter((item) => {
                return item.username.indexOf(keyword) === 0;
            })
        },
        createNewDialogMessage(content, dialogId) {
            let self = this,
                message = {},
                date = new Date();

            message.content = content;
            message.created_at = date;
            message.dialog_id = dialogId;
            message.from_user = self.username;
            message.read = true;
            message.to_user = self.getter;

            return message;
        },
        sendMessage() {
            let self = this,
                message,
                uri = '/api/1/message/',
                content = self.message + document.getElementById("img-field").innerHTML,
                params = {
                    sessionid: self.getSess(),
                    content: content,
                    login: self.getter,
                    dialog: self.dialogId
                }
            console.dir(params)
            if (self.getter === null) {
                return self.info('Выберите получателя!')
            }

            $.post(uri, params).done((data) => {
                console.log(data)
                if (data.success) {
                    self.info('Сообщение отправлено!')
                    self.message = "";
                    document.getElementById("img-field").innerHTML = "";

                    if (data.info.dialog_id !== undefined) {
                        message = self.createNewDialogMessage(content, data.info.dialog_id);
                        self.users.map(item => {
                            item.open = false;
                            if (item.username === self.getter) {
                                item.dialog_id = data.info.dialog_id;
                                item.messages.push(message);
                                item.open = true;
                                this.openedDialog = item;
                            }
                        });
                    } else {
                        message = self.createNewDialogMessage(content, self.dialogId);
                        self.users.map(item => {
                            item.open = false;
                            if (item.username === self.getter){
                                item.messages.unshift(message);
                                item.open = true; 
                                this.openedDialog = item;
                            }
                        });
                    }
                }
                console.log(self.users)
                if (data.error) {
                    console.error(data.error)
                }
            }).fail((error) => {
                console.error(error);
            });
        },
        closeModal() {
            $('#dialog_window').modal('close');
        }
    }
});

export default Dialog;
