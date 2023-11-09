$("#id_etypeBiodata").on("change", function(){  
    if ($(this).val()=="পাত্রের বায়োডাটা"){
       $(".MIM,.PIM,#DOM").show();
       $(".MIW,.PIW,#DOW").hide();
       $("#id_estayNow").on("change", function(){  
        $("#probasi,#probasiWomen").hide();
        if ($(this).val()=="প্রবাসী"){
           $("#probasi").show();
        }
       
      });
      $('#id_estayNow').trigger('change');
    }
    else if ($(this).val()=="পাত্রীর বায়োডাটা"){
       $(".MIW,.PIW,#DOW").show();
       $(".MIM,.PIM,#DOM").hide();
       $("#id_estayNow").on("change", function(){  
        $("#probasiWomen,#probasi").hide();
        if ($(this).val()=="প্রবাসী"){
           $("#probasiWomen").show();
        }
       
      });
      $('#id_estayNow').trigger('change');
    }
  });
  $('#id_etypeBiodata').trigger('change');
 
  $("select option[value='']").prop('disabled',true);
    /*district*/
    $("#id_district").change(function () {
        const url = $("#personForm").attr("data-upazilas-url");  // get the url of the `load_cities` view
        const districtId = $(this).val();  // get the selected country ID from the HTML input
        /*if(districtId==''){
          console.log("buj tid")
        }
         console.log(districtId)*/
        $.ajax({                       // initialize an AJAX request
            url: url,                    // set the url of the request (= /persons/ajax/load-cities/ )
            data: {
                'district_id': districtId       // add the country id to the GET parameters
            },
            success: function (data) {   // `data` is the return of the `load_cities` view function
                $("#id_upazila").html(data);  // replace the contents of the city input with the data that came from the server
            
            }
        });

    });
  /*বিয়ে সংক্রান্ত তথ্য*/
  /*$("#MI1,#MI2,#MI3,#MI4,#MI5").hide();*/
  $("#id_emaritalStatus").on("change", function(){  
    $("#MI1,#MI2,#MI3,#MI4,#MI5").hide();
    if ($(this).val()=="ডিভোর্সড")
       $("#MI1").show();
    else if($(this).val()=="বিবাহিত")
      $("#MI2").show();
    else if($(this).val()=="বিপত্নীক")
      $("#MI3").show();
    else if($(this).val()=="বিধবা")
      $("#MI4").show();
    else if($(this).val()=="বন্ধ্যা")
      $("#MI5").show();
   
  });
  $('#id_emaritalStatus').trigger('change');

/*Educational Qualifications>>EQ*/

$("#id_emedium").on("change", function(){  
  $(".EQC1,.EQC2,.EQC3,.EQC4,.EQC5,.EQC6").hide();
  $(".M,.AMC1,.AMC3,.AMC6").hide();
  $(".KMC1,.KMC2,.KMC3,.KMC4,.KMC5").hide();
  if ($(this).val()=="জেনারেল"){
     $(".EQC1").show();
     $("#id_essc").on("change", function(){  
      $(".EQC2,.EQC3,.EQC4,.EQC5,.EQC6").hide();
      if ($(this).val()=="না"){
         $(".EQC2").show();
      }
      else if($(this).val()=="হ্যাঁ")
      {
        $(".EQC3").show();
        $("#id_ehsc").on("change", function(){ 
          $(".EQC4,.EQC5,.EQC6").hide()
          if ($(this).val()=="না"){
             $(".EQC4").show();
          }
          else if ($(this).val()=="ডিপ্লোমা পড়েছি"){
            $(".EQC5").show();
           }
          else if($(this).val()=="হ্যাঁ"){
            $(".EQC6").show();
          }
        });
        $('#id_ehsc').trigger('change');
     }
    });
    $('#id_essc').trigger('change');
  }
  else if($(this).val()=="মাদ্রাসা"){
    $(".M").show();
    $("#id_emadrasa").on("change", function(){ 
      $(".AMC1,.AMC3,.AMC6").hide();
      $(".KMC1,.KMC2,.KMC3,.KMC4,.KMC5").hide();
      if ($(this).val()=="আলিয়া মাদ্রাসা"){
        $(".AMC1").show();
        $("#id_edhakhil").on("change", function(){  
         $(".AMC3,.AMC6").hide();
         if($(this).val()=="হ্যাঁ")
         {
           $(".AMC3").show();
           $("#id_ealim").on("change", function(){ 
             $(".AMC6").hide()
            if($(this).val()=="হ্যাঁ")
             {
             $(".AMC6").show();
             }
           });
           $('#id_ealim').trigger('change');
        }
       });
       $('#id_edhakhil').trigger('change');
      }
      else if($(this).val()=="কওমি মাদ্রাসা"){
        $(".KMC1").show();
        $("#id_edaoraya").on("change", function(){ 
          $(".KMC2,.KMC3,.KMC4,.KMC5").hide()
          if ($(this).val()=="না"){
            $(".KMC5").show();
           }
          else if ($(this).val()=="না, এখনো পড়ছি"){
            $(".KMC2").show();
           }
          else if($(this).val()=="হ্যাঁ")
          {
          $(".KMC3").show();
          $("#id_etakhassus").on("change", function(){ 
            $(".KMC4").hide()
           if($(this).val()=="হ্যাঁ")
            {
              $(".KMC4").show();
           }
          });
          $('#id_etakhassus').trigger('change');
          }
        });
        $('#id_edaoraya').trigger('change');
      }
    });
    $('#id_emadrasa').trigger('change');
   
  }

});
$('#id_emedium').trigger('change');

  /*Brother & Sister*/
  $("#id_ehavingBrother").on("change", function(){  
    $("#FB").show();
    if ($(this).val()=="ভাই নেই")
       $("#FB").hide();
  });
  $('#id_ehavingBrother').trigger('change');
  $("#id_ehavingSister").on("change", function(){  
    $("#FS").show();
    if ($(this).val()=="বোন নেই")
       $("#FS").hide();
  });
  $('#id_ehavingSister').trigger('change');
  /*start save change for required false*/ 
  $('#save_change').click(function(){
    $('input,select,textarea').prop('required', false);
  });
  /*end save change for required false*/

  /*submit button*/
  console.log($("#id_eLPVehabiour").val());
  console.log($("#id_eguardianRelation").val());
  console.log($("#id_etypeBiodata").val());
  $("input,select,textarea").on({
    blur: function(){
      if ($("#id_etypeBiodata").val()!=null && $("#id_eguardianRelation").val()!="" && $("#id_eguardianNumber").val()!="" && $("#id_eLPVehabiour").val()!=""){
        $("#submit_button").prop('disabled', false);
        $("#submit_button").removeClass("btn-disabled");
     }
     else if ($("#id_etypeBiodata").val()==null || $("#id_eguardianRelation").val()=="" || $("#id_eguardianNumber").val()=="" || $("#id_eLPVehabiour").val()==""){
      $("#submit_button").addClass("btn-disabled");
      $("#submit_button").prop('disabled', true);
     }
    },  
    mouseleave: function(){
      $(this).css("background-color", "lightblue");
      if ($("#id_etypeBiodata").val()!=null && $("#id_eguardianRelation").val()!="" && $("#id_eguardianNumber").val()!="" && $("#id_eLPVehabiour").val()!=""){
        $("#submit_button").prop('disabled', false);
        $("#submit_button").removeClass("btn-disabled");
     }
     else if ($("#id_etypeBiodata").val()==null || $("#id_eguardianRelation").val()=="" || $("#id_eguardianNumber").val()=="" || $("#id_eLPVehabiour").val()==""){
      $("#submit_button").addClass("btn-disabled");
      $("#submit_button").prop('disabled', true);
     }
    }, 
    
  });
  /*
   console.log($("#id_eguardianRelation").val());
  console.log($("#id_etypeBiodata").val());
  $("input,select").blur(function(){
    if ($("#id_etypeBiodata").val()!=null && $("#id_eguardianRelation").val()!="" && $("#id_eguardianNumber").val()!=""){
      $("#submit_button").prop('disabled', false);
      $("#submit_button").removeClass("btn-disabled");
   }
   else if ($("#id_etypeBiodata").val()==null || $("#id_eguardianRelation").val()=="" || $("#id_eguardianNumber").val()==""){
    $("#submit_button").addClass("btn-disabled");
    $("#submit_button").prop('disabled', true);
   }
  
  });*/
  /*
$("#id_eguardianNumber,#id_eguardianRelation").on({
  blur:function(){
  if ($(this).val()!=""){
    $("#submit_button").prop('disabled', false);
    $("#submit_button").removeClass("btn-disabled");
 }
 else if ($(this).val()==""){
  $("#submit_button").addClass("btn-disabled");
  $("#submit_button").prop('disabled', true);
 }
}/*,
mouseleave:function(){
  if ($(this).val()!=""){
    $("#submit_button").prop('disabled', false);
    $("#submit_button").removeClass("btn-disabled");
 }
 else if ($(this).val()==""){
  $("#submit_button").addClass("btn-disabled");
  $("#submit_button").prop('disabled', true);
 }
}/
});*/
