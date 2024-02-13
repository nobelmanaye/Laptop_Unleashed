 var laptopnum =1
 function searchLaptops(){

    var searchtext = document.getElementById("laptopSearch").value;

    

    var searchresults = document.getElementById("searchResults");

    var hp = "https://store.human-i-t.org/categories/laptop/?utm_campaign=20377544399&utm_source=google&utm_medium=cpc&utm_content=675857210156&utm_term=cheap+laptops&hsa_acc=9247694287&hsa_cam=20377544399&hsa_grp=152824510033&hsa_ad=675857210156&hsa_src=g&hsa_tgt=kwd-12171621&hsa_kw=cheap+laptops&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiAj_CrBhD-ARIsAIiMxT8EPDktS1X8He2U2Agg3lypk-CFRF78w3Nnfv4IMrHH2palqlEOEtkaAqIsEALw_wcB&page=2"

    if (searchtext.toLowerCase().includes("hp")){

      searchresults.innerHTML = "<p> Search results for <a href =" + hp + " />Click_ Here</p>"



    }
    else{

    searchresults.innerHTML = "<p> Search results for " + searchtext + " </p>";

    console.log(searchresults)

    }

 }
var laptopnum = 1; // Assuming laptopnum is defined globally

function changeLaptops() {
    var laptopsection = document.getElementById("Laptopspreview");
    var test = document.getElementById("test");
    
    laptopnum++;
    laptopsection.innerHTML = '<img src="mac' + laptopnum + '.jpg"> <button id="next1"></button>';
    test.innerHTML = "<p> changed </p>";

        // Use setTimeout to ensure the button is rendered before adding the event listener
        setTimeout(function() {
            document.getElementById("next1").addEventListener("click", changeLaptops);
        }, 0);
    }


document.getElementById("Search_button").addEventListener("click", searchLaptops);
