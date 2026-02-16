import { test, expect } from '@playwright/test';

test('API_test Get req', async ({ request }) => {

  const response = await request.get('https://petstore.swagger.io/v2/pet/1')
  const bod = await response.json();
  const response_code = response.status()

  if (response_code == 200) {

    console.log('Request successful.')
    console.log('\n',bod)
  }

  else {
    console.log('Request unsuccessful. ' + response.status())
  }

});

test('API_test Post req', async ({ request }) => {

  const jsonPayload = {

    "id": 444,
    "category": {
        "id": 444,
        "name": "new cat via 444"
    },
    "name": "new dog-updated",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

  const response = await request.post('https://petstore.swagger.io/v2/pet', {
    data: jsonPayload
  });

  if (response.status() == 200) {
    console.log('Post request successful.')

    const list = await fetch('https://petstore.swagger.io/v2/pet/findByStatus?status=available')
    const json_resp = await list.json()
    const json_resp_str = JSON.stringify(json_resp);
    const jsonPayload_str = JSON.stringify(jsonPayload);

    if (json_resp_str.includes(jsonPayload_str)){
      console.log('New resource created successfully.')
    }
    else{
      console.log('New resource was not created.', response.status())
    }
  }

  else[
    console.log('Failed to create new resource. ', response.status())
  ]

});

test('API_test Put req', async ({ request }) => {

  const jsonPayload = {
    "id": 444,
    "category": {
        "id": 1,
        "name": " new cat357 cat"
    },
    "name": "new cat cat-postman-updated",
    "photoUrls": [
        "this is the url"
    ],
    "tags": [
        {
            "id": 0,
            "name": "this is the tag"
        }
    ],
    "status": "available"
  }

  const response = await request.put('https://petstore.swagger.io/v2/pet', {
     data: jsonPayload
  });
 
  if (response.status() == 200) 
 
  {
    console.log('Put request succesful.')
    const list = await fetch('https://petstore.swagger.io/v2/pet/findByStatus?status=available')
    const json_resp = await list.json()
    const json_resp_str = JSON.stringify(json_resp);
    const jsonPayload_str = JSON.stringify(jsonPayload);

    if (json_resp_str.includes(jsonPayload_str))

    {
      console.log('Resource updated successfully.')
    }

    else{
      console.log('Resource update failed.', response.statusText())
    }

  }

  else {
    console.log('Put request unsuccesful.' +response.status())
  }
});

test('API_test Delete req', async ({ request }) => {

  const response = await request.delete('https://petstore.swagger.io/v2/pet/444')

  if (response.status() == 200) 

   {
    console.log('Delete request succesful.')
    const list = await fetch('https://petstore.swagger.io/v2/pet/444')
    if (list.status == 404){
      console.log("Resource successfully deleted.")
    }

  else
    {
        console.log("Resource was not deleted.")
  }}

  else
    {
console.log('Delete request unsuccessful. ', response.status())
  }
}
);
