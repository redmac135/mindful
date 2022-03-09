$(document).ready(function() {
    $("#id_reason :input").change(function(event) {
    if ($("#id_reason :input:checked").length > 3) {this.checked = false;}
    });
    $("#id_adjective :input").change(function(event) {
      if ($("#id_adjective :input:checked").length > 3) {this.checked = false;}
    });
  });