
// module.exports = {
//   devServer: {
//     proxy: {
//       '/record': {
//         target: 'http://localhost:5000',
//         changeOrigin: true,
//         pathRewrite: {
//           '^/record': '/record'
//         }
//       }
//     }
//   }
// };

const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

