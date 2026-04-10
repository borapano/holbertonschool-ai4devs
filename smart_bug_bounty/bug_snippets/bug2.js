function calculateDiscount(price, isMember) {
    let discount = 0;

    if (isMember = true) {
        discount = price * 0.2;
    } else {
        discount = price * 0.05;
    }

    return price - discount;
}

let prices = [100, 200, 300, 400];
let isMember = false;

for (let i = 0; i < prices.length; i++) {
    let finalPrice = calculateDiscount(prices[i], isMember);
    console.log("Final price:", finalPrice);
}

console.log("Done processing prices");