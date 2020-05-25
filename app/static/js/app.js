//----------------------------------------------------------------------  G M A P  ---------------------------------------------------------------------------
$(document).ready(function() {

    function initMap(lat, lng) {
        let position  = {lat: lat, lng : lng};
        let map = $('.map').last().get(0);
        console.log(map);
        let goMap = new google.maps.Map(map, {scrollwheel: true, zoom: 8, center: position});
        let marker = new google.maps.Marker({position: position, map: goMap})
    }

    var button = document.getElementById("search");
            //button.onclick = gearLoad;

            function gearLoad()
            {
                //montre cette saleté de spinner
                var loader = document.getElementById("loading");
                loader.style.display = "block";
                console.log("devrait afficher");
                //et précise la durée de l'évènement
                //clearTimeout(3000);
                setInterval(function(){ loader.style.display = "none"; }, 1500);

            }

    function formSubmit(callback) {
        $("form").on("submit", function(e){
            e.preventDefault();
            //alert("Form have been successfuly submitted !");
            gearLoad();
            callback();
        });
    }

    formSubmit (function() {
        //alert("What the hell is going on ?!!!");
        clearTimeout(1500);
    });

    function switcher() {
        document.getElementById("loading").style.display = "block";
    }

//--------------------------------------------------------------------------  F O R M  -----------------------------------------------------------------------

    $("form").submit(function (e) {
        gearLoad();
        //et après lance le callback pour ce qui est ci-dessous
        formSubmit();
        //$('#Map').append('<div class="map"></div>');
        //$('#Bravo').append('<div class= "col-sm-12"> <div class="bot  col-sm-6"></div> <div class="wiki col-sm-6"></div> </div>');
        //$('#Datas').append('<div class= "col-sm-12"> <div class="map col-sm-6"></div> <div class="col-sm-6> <div class="bot"></div> <div class="wiki"></div> </div> </div>');
        $('#Datas').append('<div class= "col-sm-12"> <br> <div class="row"> <div class="map col-sm-4"> </div> <div class="col-sm-8"> <aside class="bot"> </aside> <aside class="wiki"> </aside> </div> </div> </div> </div>');
        //$('#Bravo').append('<div class="wiki"></div>');
        var maps = $('.map').last();
        console.log(maps)
        var wiki = $('.wiki').last();
        var bot = $('.bot').last();

        //var objDiv = document.getElementById("wrapper"); // scroll down automaticaly

        e.preventDefault();
        let query = $("input").val();
        //console.log(query);
        $.post('/api', {
            query : query
        }).done(function (reponse) {
            //console.log(reponse);
            //gearLoad(); // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            maps.show();
            initMap(parseFloat(reponse['lat']), parseFloat(reponse['lng'])); // appel de la fonction + création GMap
            wiki.text(reponse['summary']); // appel de la fonction Wiki
            console.log(reponse['answer']);
            bot.text(reponse['answer']);
            window.scrollTo(0,document.body.scrollHeight);
            testBot();
        })
    });
/*
    function testBot() {
        var testBotContent = ("TEST du BOT // TEST du BOT // TEST du BOT");
        var button = document.getElementById("search");

        button.addEventListener("click", function() {       // l'action se déclenche quand on appuis sur le boutton
            var newBotContent = document.createElement("#Datas");  // création d'une nouvelle div
            newBotContent.innerHTML = testBotContent;                 // on indique où le contenu sera placé
            message.appendChild(newBotContent);                // on place le contenu dans la div
            return newBotContent;                              // je renvoie la 'réponse' pour la lire à l'écran
        });

    }

    function addElement () {
        var mapContent = document.getElementsByClassName("map");
        var wikiContent = document.getElementsByClassName("wiki");
        var botContent = document.getElementsByClassName("bot");
        var toPutInWrapper = mapContent; wikiContent; botContent;     // contenu de la 'réponse'
        var button = document.getElementById("search");     // j'identifie le bouton

        button.addEventListener("click", function() {       // l'action se déclenche quand on appuis sur le boutton
            var newContent = document.createElement("wrapper");  // création d'une nouvelle div
            newContent.innerHTML = toPutInWrapper;                 // on indique où le contenu sera placé
            message.appendChild(newContent);                // on place le contenu dans la div
            return newContent;                              // je renvoie la 'réponse' pour la lire à l'écran
        });
    }

    function goBottom(id){
        var element = document.getElementById(id);
        element.scrollTop = element.scrollHeight - element.clientHeight;
    }
*/
    
});