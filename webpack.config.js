const webpack = require('webpack');
const path = require('path');
const prod = process.env.NODE_ENV === 'production';
const MinifyPlugin = require('babel-minify-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const LodashPlugin = require('lodash-webpack-plugin');

const config = {
    entry: {
        main: './resources/front/main',
        common: './resources/front/common',
        inner: './resources/front/inner',
        map: './resources/front/map',
        initAdmin: './resources/front/init-admin'
    },
    output: {
        path: path.join(__dirname, "static/dist"),
        filename: prod ? '[name].entry.min.js' : '[name].entry.js',
    },
    module: {
        loaders: [{
            test:/\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
            query: {
                plugins: ['lodash'],
                presets: ['es2015']
            }
        }, {
            test: /\.html$/,
            loader: 'raw-loader'
        },
        {
            test: /\.(woff|woff2|eot|ttf)$/,
            loader: 'file-loader?name=../fonts/[name].[ext]'
        },
        {
            test: /\.css$/,
            exclude: /node_modules/,
            loader: ExtractTextPlugin.extract({
                fallback: "style-loader",
                use: [
                    {
                        loader: 'css-loader',
                        options: {
                            minimize: true
                        }
                    }
                ]}),
        }]
    },
    resolve: {
        alias: {
            vue: 'vue/dist/vue.js'
        }
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jquery: 'jquery',
            'window.jQuery': 'jquery',
            jQuery: 'jquery'
        }),
        new ExtractTextPlugin("./css/all.min.css", {
            allChunks: true
        }),
      
    ]
};

if (prod) {
    config.plugins.push(
        new MinifyPlugin(),
        new CleanWebpackPlugin(['static/dist'])
    )
}

module.exports = config;