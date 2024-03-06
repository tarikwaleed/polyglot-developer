<?php

class Cat {
    private $sound = 'Meow';
    private $isWalking = false;
    private $isEating = false;

    public function meow() {
        echo $this->sound . " ";
        return $this; // Return the object for method chaining
    }

    public function walk() {
        if (!$this->isWalking) {
            echo "Walking... ";
            $this->isWalking = true;
        }
        return $this; // Return the object for method chaining
    }

    public function eat() {
        if (!$this->isEating) {
            echo "Eating... ";
            $this->isEating = true;
        }
        return $this; // Return the object for method chaining
    }
}

// Example usage with method chaining
$myCat = new Cat();
$myCat->meow()->walk()->eat()->meow();
