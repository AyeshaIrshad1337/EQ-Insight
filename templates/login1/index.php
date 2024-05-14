<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register & Login</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <link rel="stylesheet" href="/static/PHPstyle.css">
</head>
<body>
    <div class="container" id="signup" style="display:none;">
      <h1 class="form-title">Register</h1>
      <form method="post" action="/main">

        <div id="cb-label-signup">
            <span id="toggle-state-signup">User</span>
        </div>
        <input id="cb-toggle-signup" type="checkbox" class="hide-me" aria-labelledby="cb-label-signup">
        <label for="cb-toggle-signup" class="toggle"></label>
        <input type="hidden" id="toggleStateSignup" name="toggleStateSignup" value="User">

        

        <div class="input-group">
           <i class="fas fa-user"></i>
           <input type="text" name="fName" id="fName" placeholder="First Name" required>
           <label for="fname">First Name</label>
        </div>
        <div class="input-group">
            <i class="fas fa-user"></i>
            <input type="text" name="lName" id="lName" placeholder="Last Name" required>
            <label for="lName">Last Name</label>
        </div>
        <div class="input-group">
            <i class="fas fa-envelope"></i>
            <input type="email" name="email" id="email" placeholder="Email" required>
            <label for="email">Email</label>
        </div>
        <div class="input-group">
            <i class="fas fa-lock"></i>
            <input type="password" name="password" id="password" placeholder="Password" required>
            <label for="password">Password</label>
        </div>
        <div class="input-group" id="companyNameGroup" style="display:none;">
          <i class="fas fa-building"></i>
          <input type="text" name="companyName" id="companyName" placeholder="Company Name">
          <label for="companyName">Company Name</label>
        </div>
        <input type="submit" class="btn" value="Sign Up" name="signUp" id="signupButton">

      </form>
      <p class="or">
        ----------or--------
      </p>
      <div class="icons">
        <i class="fab fa-google"></i>
        <i class="fab fa-facebook"></i>
      </div>
      <div class="links">
        <p>Already Have Account ?</p>
        <button id="signInButton">Sign In</button>
      </div>
    </div>

    <div class="container" id="signIn">
        <h1 class="form-title">Sign In</h1>
                                
        <form method="post" action="register.php">
          <div id="cb-label">
              <span id="toggle-state">User</span>
          </div>
          <input id="cb-toggle" type="checkbox" class="hide-me" aria-labelledby="cb-label">
          <label for="cb-toggle" class="toggle"></label>
          <input type="hidden" id="toggleState" name="toggleState" value="User">
          
          <div class="input-group">
              <i class="fas fa-envelope"></i>
              <input type="email" name="email" id="email" placeholder="Email" required>
              <label for="email">Email</label>
          </div>
          <div class="input-group">
              <i class="fas fa-lock"></i>
              <input type="password" name="password" id="password" placeholder="Password" required>
              <label for="password">Password</label>
          </div>
          
          <p class="recover">
            <a href="#">Recover Password</a>
          </p>
         <input type="submit" class="btn" value="Sign In" name="signIn">
        </form>
        <p class="or">
          ----------or--------
        </p>
        <div class="icons">
          <i class="fab fa-google"></i>
          <i class="fab fa-facebook"></i>
        </div>
        <div class="links">
          <p>Don't have account yet?</p>
          <button id="signUpButton" window.location.href = "/main">Sign Up</button>
        </div>
      </div>
      <script src="/static/PHPscript.js"></script>
      <script>
document.getElementById('signupForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const fName = document.getElementById('fName').value;
  const email = document.getElementById('email').value;
  const companyName = document.getElementById('companyName').value;
  const toggleStateSignup = document.getElementById('toggleStateSignup').value;

  const signupData = {
    fName,
    email,
    companyName,
    toggleStateSignup
  };

  localStorage.setItem('signupData', JSON.stringify(signupData));

  // Redirect to /main
  window.location.href = "/main";
});
</script>

</body>
</html>
