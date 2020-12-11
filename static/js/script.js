  $(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('input#input_text, textarea#textarea2').characterCounter();
  });

function roll() {
    var result = Math.floor(Math.random() * 6 + 1);
    $('result').text("Je gooide een" + result + "!");
}

dice.onclick = function () {
    roll();
};


   

  
  /*
  Collapse sidenav on small devices
  Collaps description of word
  give extra info on the read, edit and delete button with word
  Dropdown menu from Materialize
  Possibility to track amount of letters in input field
  */