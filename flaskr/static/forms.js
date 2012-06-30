var sInc = 0;
var lInc=0;

//rewrite all of our data entry forms
//ask for wdate and wcomments about the lift
//create a workout with that data using uid, don't send to db yet
//ask for lift data, create a lift associated with that workout, don't send to db yet
//ask for set data, create set, don't send to db, repeat until user says done
/*create review page and allow for any edits to be made, allow to scrap whole thing
allow to submit*/
//submit writes all table data to interface

function BuildWorkout()
{   /*this initiates our workout form, it will also clear everything back to the beginning*/
    
    //this section works through our different cases
    var theForm=document.getElementById("formInsert");
    
    //create the workout entry form
    theForm.innerHTML=  "<dt>Date: \
                      <input tabindex='1' size='4' maxlength='4' name='year' value='YYYY'>  \
              		/ <input tabindex='2' size='2' maxlength='2' name='month' value='MM'>  \
              		/ <input tabindex='3' size='2' maxlength='2' name='day' value='DD'>  \
            		<dt>Comments: \
                    <dd><textarea name='wstatus' rows=3 cols=40 ></textarea><br /> ";

    //create the add a lift button
    var alift=document.createElement("input");
    alift.type="button";
    alift.id="aLift";
    alift.onclick=Function("addLift()");
    alift.value="Add Lift";

    //create the remove a lift button
    var rlift=document.createElement("input");
    rlift.type="button";
    rlift.id="remLift";
    rlift.onclick=Function("removeLift()");
    rlift.value="Remove Lift";
    
    //need to add the option to remove a specific lift, potentially this will be remove lift
    
    //add 'em
    theForm.appendChild(alift);
    theForm.appendChild(rlift);

return false;

}
    
function addLift()
{
    //create the section of the form responsible for gathering lift input and addign sets to the lift
    var theForm=document.getElementById("formInsert"); 

    //this counter is used to keep track of multiple lifts on the form
    lInc++;
    alert("adding lift");
    //create the lType input
    var lType=document.createElement("input");
    lType.type="text";
    lType.length='20';
    lType.id='lType'+lInc;
    lType.value="WHAT TYPE OF LIFT?";
    
    //create hte lUnit input
    var lUnit=document.createElement("input");
    lUnit.type="text";
    lUnit.length='10';
    lUnit.id='lUnit'+lInc;
    lUnit.value="WHAT UNITS?";
    
    //create the add a set button
    var aSet=document.createElement("input");
    aSet.type="button";
    aSet.id="aSet"+lInc;
    aSet.onclick=Function("addSet()");
    aSet.value="Add Set";

    //create the remove a set button
    var rSet=document.createElement("input");
    rSet.type="button";
    rSet.id="rSet";
    rSet.onclick=Function("removeSet()");
    rSet.value="Remove Set";
    
    //add them to the form
    theForm.innerHTML+="<br>";
    theForm.appendChild(lType);
    theForm.appendChild(lUnit);
    theForm.innerHTML+="<br>";
    theForm.appendChild(aSet);
    theForm.appendChild(rSet);        
}

function BuildSet()
{
        var theForm=document.getElementById("formInsert");
        //create the set entry form
        var fText="<button type='button' onclick='BuildForm(\"lift\")' >Back</button> \
                    <button type='button' onclick='BuildForm(\"set\")'>Add</button> \
                     <button type='button'>Done</button>";
                    
        theForm.action="{{ url_for('enter_set')}}";

}

function clearForm(formName)
{
    /*this removes a form, given the form name*/
    docID=document.getElementById(formName);
    if (formName=="setForm")
    {
        for (x=sInc;x>0;x=x-1)
        {
            docID.removeChild(document.getElementById("set"+x));
        }
        sInc=0;
    }
    else{
       docID.remove;
    }
    
}

function AddSetForm()
{    
    /*this functions adds sets to a lift, the set is appended to setForm*/
    sInc++;
    docID=document.getElementById("setForm");
    //create the data
    var reps=document.createElement("input");
    var wgt=document.createElement("input");
    var txt1=document.createTextNode("Set "+sInc+" - Reps: ")
    var txt2=document.createTextNode(" Weight: ");
    var field=document.createElement('fieldset');

    reps.type="text";
    reps.value="Reps";
    
    wgt.type="text";
    wgt.value="Weight";
    
    field.id="set"+sInc;
    field.style.border=0;
    //append the data to the field
    field.appendChild(txt1);
    field.appendChild(reps);
    field.appendChild(txt2);
    field.appendChild(wgt);
    //append the field to the setform
    docID.appendChild(field);  
}

function RemoveSetForm()
{
    /*this removes a set from setForm as long as their are sets in the form*/
    if (sInc>0)
    {
        docID=document.getElementById("setForm");
        docID.removeChild(document.getElementById("set"+sInc));
        sInc--;
    }
}

function addToList(thing)
{
    //adds items to a list, the items are determined by "thing" which will be exercise, lift, metcon, etc
    //it then takes the entries from the form fields and populates the list
    docID=document.getElementById("theWorkout");
    if (thing=="exercise")
    {
    if (document.getElementById("wk_exDate")==null)
        {
            alert("No exercise date entered yet");
        }
    }
    
    
}
