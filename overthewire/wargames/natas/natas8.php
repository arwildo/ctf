#!/usr/bin/php
<?php

$encodedSecret = "3d3d516343746d4d6d6c315669563362";

echo base64_decode(strrev(hex2bin($encodedSecret)));

?>
