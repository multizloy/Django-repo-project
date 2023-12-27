function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let btns = document.querySelectorAll(".product-Container button");

btns.forEach(btn => {
    btn.addEventListener("click", add_To_Cart)
})
function add_To_Cart(e) {
    let product_id = e.target.value;
    let url = "add_to_cart/"

    let data = { id: product_id };
    
    fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken,
            
        },
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("num_of_items").innerHTML = data
            console.log(data);
            // alert("Added to Cart");
        })
        .catch(error => console.log(error))
}

let btn = document.querySelectorAll(".item-Container button");

btns.forEach(btn => {
    btn.addEventListener("click", remove_From_Cart)
})
function remove_From_Cart(e) {
    let product_id = e.target.value;
    let url = "remove_from_cart/"

    let data = { id: product_id };
    
    fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken,
            
        },
    })
        .then(response => response.json())
        .then(data => {
            console.log("Deleted")
            console.log(data);
            // alert("Added to Cart");
        })
        .catch(error => console.log(error))}