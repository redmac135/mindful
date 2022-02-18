$(document).ready(function() {
    $("#id_1-reason :input").change(function(event) {
    console.log($("#id_1-reason :input:checked").length)
      if ($("#id_1-reason :input:checked").length > 2) {this.checked = false;}
    });
  });