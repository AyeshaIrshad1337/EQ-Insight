<?php 

include 'connect.php';

if(isset($_POST['signUp'])){
    $firstName=$_POST['fName'];
    $lastName=$_POST['lName'];
    $email=$_POST['email'];
    $password=$_POST['password'];
    $toggleStateSignup = $_POST['toggleStateSignup']; // Retrieve toggle state for sign-up form
    $companyName = isset($_POST['companyName']) ? $_POST['companyName'] : ''; // Retrieve company name
    file_put_contents('toggle_state1.log', $toggleStateSignup . PHP_EOL, FILE_APPEND);

    if ($toggleStateSignup == 'User'){
        $checkEmail="SELECT * From applicant where email='$email'";
        $result=$conn->query($checkEmail);
        if($result->num_rows>0){
            echo "Email Address Already Exists !";
        }
        else{
            $insertQuery="INSERT INTO applicant(firstName,lastName,email,password)
                        VALUES ('$firstName','$lastName','$email','$password')";
                if($conn->query($insertQuery)==TRUE){
                    header("location: index.php");
                }
                else{
                    echo "Error:".$conn->error;
                }
        }
    }
    if ($toggleStateSignup == 'HR'){
        $checkEmail="SELECT * From applicant where email='$email'";
        $result=$conn->query($checkEmail);
        if($result->num_rows>0){
            echo "Email Address Already Exists !";
        }
        else{
            $insertQuery="INSERT INTO hr(firstName,lastName,email,password,company)
                        VALUES ('$firstName','$lastName','$email','$password','$companyName')";
                if($conn->query($insertQuery)==TRUE){
                    header("location: index.php");
                }
                else{
                    echo "Error:".$conn->error;
                }
        }

    }
   

}

if(isset($_POST['signIn'])){
   $email=$_POST['email'];
   $password=$_POST['password'];
   $toggleState = $_POST['toggleState'];
   file_put_contents('toggle_state.log', $toggleState . PHP_EOL, FILE_APPEND);
   
    if ($toggleState == 'User'){
        $sql="SELECT * FROM applicant WHERE email='$email' and password='$password' ";
        $result=$conn->query($sql);
        if($result->num_rows>0){
            session_start();
            $row=$result->fetch_assoc();
            if ($toggleState == 'User'){
                $_SESSION['toggleState'] = 'User';
                $_SESSION['email']=$row['email'];
                header("Location: homepage.php");
            } elseif ($toggleState == 'HR') {
                $_SESSION['toggleState'] = 'HR';
                $_SESSION['email']=$row['email'];
                header("Location: homepage.php");
            }
            exit();
        }
        else{
            echo "Not Found, Incorrect Email or Password";
        }  
    }

    if ($toggleState == 'HR'){
        $sql="SELECT * FROM hr WHERE email='$email' and password='$password' ";
        $result=$conn->query($sql);
        if($result->num_rows>0){
            session_start();
            $row=$result->fetch_assoc();
            if ($toggleState == 'User'){
                $_SESSION['toggleState'] = 'User';
                $_SESSION['email']=$row['email'];
                header("Location: homepage.php");
            } elseif ($toggleState == 'HR') {
                $_SESSION['toggleState'] = 'HR';
                $_SESSION['email']=$row['email'];
                header("Location: homepage.php");
            }
            exit();
        }
        else{
            echo "Not Found, Incorrect Email or Password";
        }
    }
   
   

}
?>