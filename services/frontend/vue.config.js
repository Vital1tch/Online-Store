const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    watchFiles: ['src/**/*', 'public/**/*'],
  },
})
