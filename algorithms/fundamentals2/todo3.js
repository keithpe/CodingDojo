//****************************************************************************
// Rockin’ the Dojo Sweatshirt
//****************************************************************************
// Ever since you arrived at the Dojo, you wanted one of those cool Coding 
// Dojo sweatshirts – maybe even more than one. 
// 
// Let’s say they cost $20 (including tax), but friendly Josh gives a 9% 
// discount if you buy two, a nice 19% discount if you buy three, or a sweet 
// 35% discount if you buy four or more. 
// 
// He only accepts cash and says he 
// doesn’t have coins, so you should round up to the nearest dollar. 
// 
// Build function sweatshirtPricing(num) that, given a number of 
// sweatshirts, returns the cost.
//****************************************************************************

function sweatshirtPricing(num) {
    let cost = 0;
    if (num == 1) {
        cost = 20
    } else if (num == 2) {
        cost = Math.ceil((20 - (20 * .09)) * 2)
    } else if (num == 3) {
        cost = Math.ceil((20 - (20 * .19)) * 3)
    } else {
        cost = Math.ceil((20 * .35) * num)
    }
    return cost
}

console.log("\n**** sweatshirtPricing ****")
console.log(sweatshirtPricing(1))
console.log(sweatshirtPricing(2))
console.log(sweatshirtPricing(3))
console.log(sweatshirtPricing(4))


//****************************************************************************
// Clock Hand Angles, Revisited
//****************************************************************************
// Return to your previous clockHandAngles solution. Allow fractional values 
// for input seconds, but change your implementation to print only integer 
// values for angles (in degrees) of the various hands.
//****************************************************************************

function clockHandAngles(seconds) {

}

console.log("\n**** clockHandAngles (revisited) ****")
clockHandAngles(3600)