const app = require('./app');
const { Eureka } = require('eureka-js-client');

const PORT = Number(process.env.PORT) || 8083;

const eurekaClient = new Eureka({
  instance: {
    app: 'MEETING',
    hostName: 'localhost',
    ipAddr: '127.0.0.1',
    statusPageUrl: `http://localhost:${PORT}/info`,
    healthCheckUrl: `http://localhost:${PORT}/health`,
    port: {
      '$': PORT,
      '@enabled': true,
    },
    vipAddress: 'meeting',
    dataCenterInfo: {
      '@class': 'com.netflix.appinfo.InstanceInfo$DefaultDataCenterInfo',
      name: 'MyOwn',
    },
  },
  eureka: {
    host: 'localhost',
    port: 8761,
    servicePath: '/eureka/apps/',
  },
});

app.listen(PORT, () => {
  console.log(`meeting microservice running on http://localhost:${PORT}`);
  console.log(`Swagger UI: http://localhost:${PORT}/swagger-ui`);
  eurekaClient.start((error) => {
    if (error) {
      console.error('Eureka registration error:', error);
    } else {
      console.log(`MEETING registered with Eureka on port ${PORT}`);
    }
  });
});