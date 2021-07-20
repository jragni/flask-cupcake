"use strict"
const BASE_API_URL = 'http://localhost:5000/api/';
const $cupcakeList = $('#cupcake-list');

/** getCupcakes
 * Description: function that requests cupcake data from API and displays it on the DOM
 */

async function getCupcakes() {
    let response = await axios.get(`${BASE_API_URL}cupcakes`);  // [{Cupcakes}]
    return response.data.cupcakes
}

async function listCupcakes(){
    const cupcakes = await getCupcakes();
    console.log(cupcakes)
    cupcakes.forEach( cupcake => {
        const $li = $("<li>");
        $cupcakeList.append( $li.text(cupcake.flavor));
    })
}

/** main
 * Description: runs on start
 */

function main(){
    listCupcakes()
}

main();