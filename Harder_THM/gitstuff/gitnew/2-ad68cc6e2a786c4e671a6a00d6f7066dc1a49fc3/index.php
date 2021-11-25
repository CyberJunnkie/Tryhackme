<?php
session_start();
require("auth.php");
$login = new Login;
$login->authorize();

phpinfo();
?>
