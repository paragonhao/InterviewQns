//Scala Intro Tutorial

//Type initialization

val twoClubs: Int = 2
val threeClubs: Int = 3
val fourClubs: Int = 4

val playerA: String = "Alex"
val playerB: String = "Chen"
val playerC: String = "Umberto"	

var aceClubs: Int = 1
var aceDiamonds: Int = 1
var aceHearts: Int = 1
var aceSpades: Int = 1

// Create a mutable variable for Alex as player A
var playerA: String = "Alex"

// Change the point value of A♦ from 1 to 11
var aceDiamonds: Int = 11

// Calculate hand value for J♣ and A♦
println(jackClubs + aceDiamonds)

// Calculate hand values
val handPlayerA: Int = queenDiamonds + threeClubs + fiveSpades + aceHearts
val handPlayerB: Int = kingHearts + jackHearts

// Find and print the maximum hand value
println(maxHand(handPlayerA, handPlayerB))

// Create and parameterize an array for a round of Twenty-One
val hands: Array[Int] = new Array[Int](3)

// Initialize the first player's hand in the array
hands(0) = tenClubs + fourDiamonds

// Initialize the second player's hand in the array
hands(1) = nineSpades + nineHearts

// Initialize the third player's hand in the array
hands(2) = twoClubs + threeSpades

// Create, parameterize, and initialize an array for a round of Twenty-One
val hands = Array(tenClubs + fourDiamonds,
              nineSpades + nineHearts,
              twoClubs + threeSpades)

// Initialize player's hand and print out hands before each player hits
hands(0) = tenClubs + fourDiamonds
hands(1) = nineSpades + nineHearts
hands(2) = twoClubs + threeSpades
hands.foreach(println)

// Add 5♣ to the first player's hand
hands(0) = hands(0) + fiveClubs

// Add Q♠ to the second player's hand
hands(1) = hands(1) + queenSpades

// Add K♣ to the third player's hand
hands(2) = hands(2) + kingClubs

// Print out hands after each player hits
hands.foreach(println)

// Initialize a list with an element for each round's prize
val prizes = List(10, 15, 20, 25, 30)
println(prizes)

// Prepend to prizes to add another round and prize
val newPrizes = 5 :: prizes
println(newPrizes)

// Initialize a list with an element each round's prize
val prizes = 10::15::20::25::30::Nil
println(prizes)


// The original NTOA and EuroTO venue lists
val venuesNTOA = List("The Grand Ballroom", "Atlantis Casino", "Doug's House")
val venuesEuroTO = "Five Seasons Hotel" :: "The Electric Unicorn" :: Nil

// Concatenate the North American and European venues
val venuesTOWorld = venuesNTOA:::venuesEuroTO

// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + fourSpades

// Congratulate the player if they have reached 21
if(hand == 21) {
  println("Twenty-One!")
}


// example of functional programming
// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + fiveSpades

// Inform a player where their current hand stands
val informPlayer: String = {
  if (hand > 21)
    "Bust! :("
  else if (hand ==21)
    "Twenty-One! :)"
  else
    "Hit or stay?"
}

// Print the message
print(informPlayer)


// Find the number of points that will cause a bust
def pointsToBust(hand: Int): Int = {
  // If the hand is a bust, 0 points remain
  if(hand>21)
    0
  // Otherwise, calculate the difference between 21 and the current hand
  else
    21 - hand
}

// Test pointsToBust with 10♠ and 5♣
val myHandPointsToBust = pointsToBust(tenSpades + fiveClubs)
println(myHandPointsToBust)


// Define counter variable
var i = 0

// Define the number of loop iterations
var numRepetitions = 3

// Loop to print a message for winner of the round
while (i < numRepetitions) {
  if (i < 2)
    println("winner")
  else
    println("chicken dinner")
  // Increment the counter variable
  i +=1
}


// Loop over a collection with while
// Define counter variable
var i = 0

// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands
while (i< hands.length) {
  // Find and print number of points to bust
  println(pointsToBust(hands(i)))
  // Increment the counter variable
  i += 1
}


// Find the number of points that will cause a bust
def pointsToBust(hand: Int) = {
  // If the hand is a bust, 0 points remain
  if (bust(hand))
    println(0)
  // Otherwise, calculate the difference between 21 and the current hand
  else
    println(21 - hand)
}

// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands, finding each hand's number of points to bust
hands.foreach(pointsToBust)



