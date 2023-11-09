$(document).ready(function () {
    $(".bk").click(function(){
        $(".bkash").toggle();
        $("#html").prop("checked", true);
        $("#css").prop("checked", false);
        $("#java").prop("checked", false);
        $(".rocket,.nagad").hide();
      });
      $(".roc").click(function(){
        $(".rocket").toggle();
        $("#css").prop("checked", true);
        $("#html").prop("checked", false);
        $("#java").prop("checked", false);
        $(".bkash,.nagad").hide();
      });
      $(".nag").click(function(){
        $(".nagad").toggle();
        $("#java").prop("checked", true);
        $("#css").prop("checked", false);
        $("#html").prop("checked", false);
        $(".rocket,.bkash").hide();
      });
    $("#Ebtn").click(function () {
      if ($("#HbkashNumber").val() != '' && $("#HbkashId").val()!='') {
        $("#HrocketNumber,#HrocketId,#HnagadNumber,#HnagadId").prop('required', false);
      }
      else if($("#HrocketNumber").val()!='' && $("#HrocketId").val()!='') {
        $("#HbkashNumber,#HbkashId,#HnagadNumber,#HnagadId").prop('required', false);
       
      }
      else if ($("#HnagadNumber").val() != '' && $("#HnagadId").val() != '') {
        $("#HbkashNumber,#HbkashId,#HrocketNumber,#HrocketId").prop('required', false);
      }
      else{
        $(".bkash").show();
        swal({
          title: "পেমেন্ট করুন!",
          text: "বিকাশ, রকেট বা নগদ যেকোনো একটি মাধ্যমে পেমেন্ট করুন!",
          icon: "warning",
          dangerMode: true,
        })
        /*swal("বিকাশ, রকেট বা নগদ যেকোনো একটি মাধ্যমে পেমেন্ট করুন!");
        /alert("বিকাশ, রকেট বা নগদ যেকোনো একটি মাধ্যমে পেমেন্ট করুন!")*/
      }
    });
  });