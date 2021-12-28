
<script>


document.addEventListener('DOMContentLoaded', function() {
    document.querySelector("form").onsubmit = function() {
        // Send a GET request to the URL
        const nameofrecipe = document.getElementById('foodname').value
        console.log(nameofrecipe);
        fetch('https://api.spoonacular.com/recipes/complexSearch?query=pasta&maxFat=25&number=2&apiKey=fae840d1e0ac4a73a10dcddb3537deab')
        // Put response into json form
        .then(response => response.json())
        .then(data => {
        // Log data to the console
        console.log(data);
       

        // Display message on the screen
        document.getElementById('title').innerHTML = "<h1>" + data.results[0].title + "</h1>";
        document.getElementById('photo').innerHTML = "<img src = "+ data.results[0].image +" width='400' />";
        //document.querySelector('body').innerHTML = data.results[0].nutrition
        return false;
    });

    }
    
});
</script>