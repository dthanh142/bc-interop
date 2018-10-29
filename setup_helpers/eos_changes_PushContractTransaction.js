Eos = require('eosjs') // Eos = require('./src')
const util = require('util')

const httpEndpointAddress = process.argv[2];
const wif = process.argv[3];
const contract_account = process.argv[4];
const contract_function = process.argv[5];
const authorization_actor = process.argv[6];
const authorization_permission = process.argv[7];
const data_values = JSON.parse(process.argv[8]);

eos = Eos({
  keyProvider: wif,
  httpEndpoint: httpEndpointAddress,
  // Added this line to be able to interact with jungle testnet
  chainId: '038f4b0fc8ff18a4f0842a8f0564611f6e96e8535901dd45e43ac8691a1c4dca',
})


eos.transaction({
  actions: [
    {
      account: contract_account,
      name: contract_function,
      authorization: [{
        actor: authorization_actor,
        permission: authorization_permission
      }],
      data: data_values
    }
  ]
}).then(function (value){
        // Added this line to get tx id back
        console.log("This is the return from tx: " + value.transaction_id);
        return value;
      }).catch(function (e) {
      console.error(e);
      process.exit(1);
      })