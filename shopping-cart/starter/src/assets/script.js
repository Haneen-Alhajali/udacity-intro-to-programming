/* Create an array named products which you will use to add all of your product object literals that you create in the next step. */
const products = [];

/* Create 3 or more product objects using object literal notation 
Each product should include five properties
- name: name of product (string)
- price: price of product (number)
- quantity: quantity in cart should start at zero (number)
- productId: unique id for the product (number)
- image: picture of product (url string)
*/

/* Images provided in /images folder. All images from Unsplash.com
- cherry.jpg by Mae Mu
- orange.jpg by Mae Mu
- strawberry.jpg by Allec Gomes
*/

// Product 1: Cherry
const cherry = {
    name: "Cherry",
    price: 3.99,
    quantity: 0,
    productId: 100,
    image: "./images/cherry.jpg"
};

// Product 2: Orange
const orange = {
    name: "Orange",
    price: 2.49,
    quantity: 0,
    productId: 101,
    image: "./images/orange.jpg"
};

// Product 3: Strawberry
const strawberry = {
    name: "Strawberry",
    price: 4.29,
    quantity: 0,
    productId: 102,
    image: "./images/strawberry.jpg"
};

// Add products to products array
products.push(cherry, orange, strawberry);

/* Declare an empty array named cart to hold the items in the cart */
const cart = [];

/* Helper function to find a product by productId */
function getProductById(productId) {
    return products.find(p => p.productId === productId);
}

/* Create a function named addProductToCart that takes in the product productId as an argument
- addProductToCart should get the correct product based on the productId
- addProductToCart should then increase the product's quantity
- if the product is not already in the cart, add it to the cart
*/
function addProductToCart(productId) {
    // Find the product by productId
    const product = getProductById(productId);
    
    if (product) {
        // Increase the product quantity
        product.quantity += 1;
        
        // Check if product is already in cart
        const productInCart = cart.find(p => p.productId === productId);
        
        // If product is not in cart, add it
        if (!productInCart) {
            cart.push(product);
        }
    }
}

/* Create a function named increaseQuantity that takes in the productId as an argument
- increaseQuantity should get the correct product based on the productId
- increaseQuantity should then increase the product's quantity
*/
function increaseQuantity(productId) {
    const product = getProductById(productId);
    
    if (product) {
        product.quantity += 1;
    }
}

/* Create a function named decreaseQuantity that takes in the productId as an argument
- decreaseQuantity should get the correct product based on the productId
- decreaseQuantity should decrease the quantity of the product
- if the function decreases the quantity to 0, the product is removed from the cart
*/
function decreaseQuantity(productId) {
    const product = getProductById(productId);
    
    if (product) {
        product.quantity -= 1;
        
        // If quantity reaches 0, remove product from cart
        if (product.quantity === 0) {
            removeProductFromCart(productId);
        }
    }
}

/* Create a function named removeProductFromCart that takes in the productId as an argument
- removeProductFromCart should get the correct product based on the productId
- removeProductFromCart should update the product quantity to 0
- removeProductFromCart should remove the product from the cart
*/
function removeProductFromCart(productId) {
    const product = getProductById(productId);
    
    if (product) {
        // Reset product quantity to 0
        product.quantity = 0;
        
        // Find the index of the product in cart
        const productIndex = cart.findIndex(p => p.productId === productId);
        
        // Remove product from cart if found
        if (productIndex !== -1) {
            cart.splice(productIndex, 1);
        }
    }
}

/* Create a function named cartTotal that has no parameters
- cartTotal should iterate through the cart to get the total cost of all products
- cartTotal should return the total cost of the products in the cart
Hint: price and quantity can be used to determine total cost
*/
function cartTotal() {
    let total = 0;
    
    for (const product of cart) {
        total += product.price * product.quantity;
    }
    
    return total;
}

// Global variable to track total amount paid
let totalPaid = 0;

/* Create a function named pay that takes in an amount as an argument
- amount is the money paid by customer
- pay will return a negative number if there is a remaining balance
- pay will return a positive number if money should be returned to customer
Hint: cartTotal function gives us cost of all the products in the cart
*/
function pay(amount) {
    // Add the new payment to totalPaid
    totalPaid += amount;
    
    const cartTotalAmount = cartTotal();
    const difference = totalPaid - cartTotalAmount;
    
    // If customer has paid enough (difference >= 0)
    if (difference >= 0) {
        // Empty the cart since transaction is complete
        // Note: emptyCart() will reset totalPaid to 0 for next transaction
        const changeDue = difference; // Save the change amount before clearing
        emptyCart();
        return changeDue; // Return the change due
    } else {
        // Customer hasn't paid enough, return negative balance
        return difference;
    }
}

/* Create a function called emptyCart that empties the products from the cart */
function emptyCart() {
    // Reset quantity for all products in cart to 0
    for (const product of cart) {
        product.quantity = 0;
    }
    
    // Clear the cart array
    cart.length = 0;
    
    // Reset totalPaid to 0 for next transaction
    totalPaid = 0;
}

/* Place stand out suggestions here (stand out suggestions can be found at the bottom of the project rubric.)*/
/* Uncomment the currency converter in front.js to use this function */
function currency(currencyCode) {
    // This function would handle currency conversion
    // For now, it's a placeholder as currency conversion logic 
    // would require an API or conversion rates
    console.log(`Currency changed to: ${currencyCode}`);
}

/* The following is for running unit tests. To fully complete this project, it is expected that all tests pass. Run the following command in terminal to run tests npm run test */
module.exports = {
    products,
    cart,
    addProductToCart,
    increaseQuantity,
    decreaseQuantity,
    removeProductFromCart,
    cartTotal,
    pay,
    emptyCart,
    // Uncomment the following line if completing the currency converter bonus
    currency
}