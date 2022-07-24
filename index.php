<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
<head> 
<body>


    <?php require_once 'process.php'; ?>
    <div class="row">
    <form action="process.php" method="POST">
        <div class="form-group">
        <label>Name</label><br/>
        <input type="text" name="name" class="form-control" placeholder="Enter Your Name"><br/>
        </div>

        <div class="form-group">
        <label>Location</label><br/>
        <input type="text" name="location" class="form-control" placeholder="Enter Your Location"><br/>
        </div>

        <div class="form-group">
        <br/>
        <button type="submit" name="save">Save</button> 
        </div>
    </form>
    </div>    


<body>
<html>