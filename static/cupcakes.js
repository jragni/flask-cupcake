"use strict"
const BASE_API_URL = 'http://localhost:5000/api/';
const $cupcakeList = $('#cupcake-list');
const $submitBtn = $('#submit-btn')
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

$submitBtn.on('click', submitCallback)

async function submitCallback(evt) {
    console.log('we made it -- submit')
    evt.preventDefault();
    // get form values
    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image = $("#image").val();
    let data = {flavor, size, rating, image};
    let response = await axios.post(`${BASE_API_URL}cupcakes`, data);
    console.log(response);
}


// TODO: append dom with new 

/** main
 * Description: runs on start
 */

function main(){
    listCupcakes()
}

main();