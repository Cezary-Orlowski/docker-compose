<?php
$db = JFactory::getDBO();
// id - numer rekordu, ktory chcemy wyświetlic
$db->setQuery("SELECT encode(photo, 'base64') AS photo FROM images WHERE id=3"); 
$img = $db->loadResult();

$data = base64_decode($img);

echo '<img src="data:image/png;base64,' . $data . '" />';
?>