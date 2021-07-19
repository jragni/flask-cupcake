"use strict"
const BASE_API_URL = 'http://localhost:5000/api/';

async function getCupcakes() {
    let response = await axios.get(`${BASE_API_URL}cupcakes`);
    

      
}