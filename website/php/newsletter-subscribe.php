<?php
/*
Name: 			Newsletter Subscribe
Written by: 	Okler Themes - (http://www.okler.net)
Version: 		4.8.0
*/

include('./mailchimp/mailchimp.php'); 

use \DrewM\MailChimp\MailChimp;

// Step 1 - Set the apiKey - How get your Mailchimp API KEY - http://kb.mailchimp.com/article/where-can-i-find-my-api-key
$apiKey 	= '7f73c53aa82d00dd9ad3755224504e38-us11';

// Step 2 - Set the listId - How to get your Mailchimp LIST ID - http://kb.mailchimp.com/article/how-can-i-find-my-list-id
$listId 	= '2f2d232acc';

if (isset($_POST['email'])) {
	$email = $_POST['email'];
} else if (isset($_GET['email'])) {
	$email = $_GET['email'];
} else {
	$email = '';
}

$MailChimp = new MailChimp($apiKey);

$result = $MailChimp->post('lists/' . $listId . '/members', array(
	'email_address' => $email,
	'merge_fields'  => array('FNAME'=>'', 'LNAME'=>''), // Step 3 (Optional) - Vars - More Information - http://kb.mailchimp.com/merge-tags/using/getting-started-with-merge-tags
	'status' 		=> 'subscribed'
));

if ($result['id'] != '') {
	$arrResult = array('response'=>'success');	
} else {
	$arrResult = array('response'=>'error','message'=>$result['detail']);
}

echo json_encode($arrResult);