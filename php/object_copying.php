<?php
// Shallow Copying START
$person1 = [
    'name' => 'Ahmed',
    'age' => 23,
    'children' => ['Mohamed', 'Mona'],
];

$person2 = $person1;

$person1['name'] = 'Ali';
$person1['children'][0] = 'Mario';

echo "<pre>";
echo "Shallow Copying Example:\n";
echo "<span style='color: blue;'>\$person1:</span> ";
echo "<span style='color: green;'>" . print_r($person1, true) . "</span>";
echo "<span style='color: blue;'>\$person2:</span> ";
echo "<span style='color: green;'>" . print_r($person2, true) . "</span>";
echo "</pre>";
// Shallow Copying END

// Deep Copying START
function deepCopy($array)
{
    return unserialize(serialize($array));
}

$person1 = [
    'name' => 'Ahmed',
    'age' => 23,
    'children' => ['Mohamed', 'Mona'],
];

$person2 = deepCopy($person1);

$person1['name'] = 'Ali';
$person1['children'][0] = 'Sara';

echo "<pre>";
echo "Deep Copying Example:\n";
echo "<span style='color: blue;'>\$person1:</span> ";
echo "<span style='color: green;'>" . print_r($person1, true) . "</span>";
echo "<span style='color: blue;'>\$person2:</span> ";
echo "<span style='color: green;'>" . print_r($person2, true) . "</span>";
echo "</pre>";
// Deep Copying END

// Value Semantics START
$a = 5;
$b = $a;

$b = 10;

echo "<pre>";
echo "Value Semantics Example:\n";
echo "<span style='color: blue;'>\$a:</span> <span style='color: red;'>" . $a . "</span>\n";
echo "<span style='color: blue;'>\$b:</span> <span style='color: red;'>" . $b . "</span>";
echo "</pre>";
// Value Semantics END
