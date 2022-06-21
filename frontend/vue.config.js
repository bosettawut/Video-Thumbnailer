module.exports = {
    transpileDependencies: ["vuetify"],
    devServer: {
      host: "0.0.0.0",
      port: 8080,
      https: false,
    //   proxy: {
    //     "/api": {
    //       target: "http://127.0.0.1",
    //     },
    //   },
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
        "Access-Control-Allow-Headers":
          "X-Requested-With, content-type, Authorization",
      },
    },
  
  };