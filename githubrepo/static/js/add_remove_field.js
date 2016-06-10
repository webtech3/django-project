$(document).ready(function(){

  var counter = 2;

  $("#addButton").click(function () {
        
    var newTextBoxDiv = $(document.createElement('div'))
     .attr("id", 'TextBoxDiv' + counter);
              
    newTextBoxDiv.after().html(
      '<input type="textbox" class="form-control" placeholder="Github User & Repo, e.g: s062009/testingrepo" name="repo_url' + counter + 
      '" id="textbox' + counter + '" value="" required><br>');
          
    newTextBoxDiv.appendTo("#TextBoxesGroup");

      
    counter++;
  });

  $("#removeButton").click(function () {
    if(counter==1){
        alert("No more textbox to remove");
        return false;
   }   
    
  counter--;

    $("#TextBoxDiv" + counter).remove();

  });
});