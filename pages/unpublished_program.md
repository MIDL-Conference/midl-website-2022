---
title: "Program at a Glance"
page_class: "keynotes"
---

# Program at a glance

<style>
#program, #program th, #program td {
    border: 1px solid gray;
    font-size: 85%;
    border-collapse: separate;
    border-spacing: 1px;
    color: #222222;
}
@media (min-width: 1200px) {
    #program {
        margin-left: -50px;
        margin-right: -50px;
    }
}
#program th, #program td {
  padding: 5px;
  text-align: left;
}
#hide-show-timezones {
    font-size: 90%;
    margin-top: 1em;
    padding: 0 6px;
    display: flex;
    flex: 0 0 auto;
    flex-direction: row;
    flex-wrap: wrap;
    white-space: nowrap;
    justify-content: space-between;
}
#hide-show-timezones input.largerCheckbox {
    transform : scale(1.5);
}
#hide-show-timezones label {
    padding: 0 4px 0 8px;
}
#program div, #program a {
    color: white;
}
#program a:hover {
    text-decoration: underline;
}
#r00{
      background-color: #96B6BD;
 /*   appearance: none;*/
    box-shadow: 0 0 0px 8px gold;

  clip-path: polygon(-20% 0%, 100% 0%, 100% 100%, -20% 100%); /*left*/

}
#r00t{
      background-color: #96B6BD;
        box-shadow: 0 0 0px 8px gold;
        clip-path: polygon(-20% -20%, 100% -20%, 100% 100%, -20% 100%); /*top-left*/
    }


#t01b {
  background-color: #BDC0BF;
    box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
  font-weight: 350
}

#t01t {
  background-color: #BDC0BF;
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
  font-weight: 350
}
#r00b{
      background-color: #96B6BD;
        box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(-20% 0%, 100% 0%, 100% 120%, -20% 120%); /*bottom--*/
    }

#r01 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #BDC0BF;
  font-weight: 350

}

#r05 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #C4DFB3;
}

#r06 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #F9D368;
}

#r02 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #D9A9BC;
}
#r03 {
    box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;
  background-color: #CDDFF0;
}
#t00 {
  background-color: #96B6BD;
}
#t01 {
  background-color: #BDC0BF;
  font-weight: 350
}

#cshort_v {
  background-color: #B9A3BE;
}
#clong_v {
  background-color: #B8CEDB;
}

#cmentor {
  background-color: #E8B8A2;
}
#cspecial {
  background-color: #74A1A7;
}
    #cspecial_t{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
      border: 1px;}
     #cspecial_tr{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 120% -20%, 120% 100%, 0% 100%); /*top-right*/
      border: 1px;}
    #cspecial_br{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 120%, 0% 120%); /*bottom-right*/
      border: 1px;}

    #cspecial_b{   background-color: #74A1A7; box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
      border: 1px;}

    #title_legend{font-weight:300; font-size: 100%; text-align:left; color:white; padding-left: 6px; padding-right: 6px; white-space: nowrap; }
    #text_legend{font-weight:150; font-size: 80%; text-align:left; padding-left: 6px; }
    #cbreak_r{   background-color: #AEAEAE; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #cbreak{   background-color: #AEAEAE; }
    #cbreak div, #cbreak_r div { color: #222222; }

    #clong_tr{   background-color: #0083AC; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 120% -20%, 120% 100%, 0% 100%); /*top-right*/
      border: 1px;}

    #clong_t{   background-color: #0083AC; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
      border: 1px;}

    #clong_r{   background-color: #0083AC; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #clong{   background-color: #0083AC;}

    #ckeynote_r{   background-color: #016297; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #ckeynote{   background-color: #016297;}

    #cshort_r{   background-color: #82538B; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #cshort{   background-color: #82538B;}

    #cposter_r{   background-color: #248F85; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
      border: 1px;}

    #cposter_br{   background-color: #248F85; box-shadow: 0 0 0px 8px gold;
      clip-path: polygon(0% 0%, 120% 0%, 120% 120%, 0% 120%); /*bottom-right*/
      border: 1px;}

    #cposter_b{   background-color: #248F85; box-shadow: 0 0 0px 8px gold;
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
      border: 1px;}

    #cposter{   background-color: #248F85;}


</style>
<script>
jQuery(document).ready(function($) {
    $('input[type= checkbox ]').click(function() {
        let index = $(this).attr('name').substr(3);
        index--;
        $('table tr').each(function() {
            $('td:eq(' + index + ')',this).toggle();
        });
        $('th.' + $(this).attr('name')).toggle();
    });
});
</script>
<!--
  clip-path: polygon(0% 0%, 100% 0%, 100% 120%, 0% 120%); /*bottom*/
      clip-path: polygon(0% -20%, 100% -20%, 100% 120%, 0% 120%); /*bottom-top*/
      clip-path: polygon(0% -20%, 100% -20%, 100% 100%, 0% 100%); /*top*/
      clip-path: polygon(0% 0%, 120% 0%, 120% 100%, 0% 100%); /*right*/
  clip-path: polygon(0% 0%, 120% 0%, 120% 120%, 0% 120%); /*bottom-right*/
-->
<!-- <table id="program">
	<thead>
		<tr>
			<th class="col1" id='t01'>PDT UTC-7</th>
			<th class="col2" id='t01'>CET UTC+1</th>
			<th class="col3" colspan="1" id='t00'><b>5th July</b></th>
			<th class="col4" colspan="1" id='t00'><b>6th July</b></th>
			<th class="col5" colspan="1" id='t00'><b>7th July</b></th>
			<th class="col6" colspan="1" id='t00'><b>8th July</b></th>
			<th class="col7" colspan="1" id='t00'><b>9th July</b></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<th class="col1" ></th>
			<th class="col2" ></th>
			<th ></th>
			<th colspan="3" >Registration, Poster Setup</th>
			<th ></th>
		</tr>
		<tr>
			<th class="col1"  rowspan="10" id='t01'>01.15-09.00</th>
			<th class="col2" rowspan="10" id='t01'>10.15-18.00</th>
			<th class="col3" rowspan="3"><a href='tutorials.html'>Tutorial I</a></th>
			<th class="col4" id='cmentor'>Welcome and Orals</th>
			<th class="col5" id='cmentor'>Orals</th>
			<th class="col6" id='cmentor'>Orals</th>
			<th class="col7"  rowspan="9" '><a href='doctoral-symposium.html'>Doctoral Symposium</a></th>
		</tr>
		<tr>
			<th colspan="3" >Coffee break</th>
		</tr>
		<tr>
			<th colspan="3" id='clong_v' >Poster session onsite and virtual</th>
		</tr>
		<tr>
    <th rowspan="2"></th>
			<th colspan="3">Lunch</th>
		</tr>
		<tr>
      <th colspan="1" id='cmentor' ></th>
			<th colspan="3" id='cmentor' >Orals</th>
		</tr>
		<tr>
    	<th rowspan="3" id='cshort_v'>Tutorial II</th>
			<th colspan="3" id='cshort_v'>Keynotes</th>
		</tr>
		<tr>
			<th colspan="3">Coffee break</th>
		</tr>
		<tr>
			<th colspan="3" id='cmentor'>Orals</th>
		</tr>
		<tr>
    <th colspan="1"></th>
			<th colspan="3"  id='clong_v' >Poster Session onsite and virtual</th>
		</tr>
		<tr>
			<th class="col1" ></th>
			<th class="col2"></th>
      <th class="col3" ></th>
			<th class="col4" >Get together</th>
			<th class="col5">Gala Dinner</th>
			<th class="col6" >Closing ceremony</th>
		</tr>
	</tbody>
</table> -->

<!-- <form
id="hide-show-timezones">
<div>
  <input
    class="largerCheckbox"
    type="checkbox"
    id="hs-col1"
    name="col1"
    checked="checked">
  <label for="hs-col1">Hide/Show
    UTC-7</label>
</div>
<div>
  <input
    class="largerCheckbox"
    type="checkbox"
    id="hs-col2"
    name="col2"
    checked="checked">
  <label for="hs-col2">Hide/Show
    UTC +1</label>
</div>
</form>

<hr> -->


<table cellspacing="0" border="0">
	<colgroup span="6" width="138"></colgroup>
	<tr>
        <td><br></td>
		<td id='t00'>July 5, 2022</td>
		<td id='t00'>July 6, 2022</td>
		<td id='t00'>July 7, 2022</td>
		<td id='t00'>July 8, 2022</td>
		<td id='t00'>July 9, 2022</td>
	</tr>
	<tr>
		<td id='t01' rowspan=3 height="80" align="center">09:00 - 10:00</td>
		<td id='cposter' align="center" rowspan=9><a href='tutorials.html'>Tutorial I</a></td>
		<td colspan=3 align="center" id='cbreak' rowspan=2>Registration, Poster Setup</b></td>
		<td rowspan=21 align="center"><a href='doctoral-symposium.html'>Doctoral Symposium</a></td>
	</tr>
	<tr>
		<td><br></td>
	</tr>
	<tr>
		<td align="center">Welcome</td>
		<td id='cmentor' align="center" rowspan=3>Oral 2.1</td>
		<td id='cmentor' align="center" rowspan=3>Oral 3.1</td>
		<td><br></td>
	</tr>
	<tr>
		<td id='t01' rowspan=3 height="80" align="center" >10:00 - 11:00</td>
		<td id='cmentor' align="center" rowspan=2 >Oral 1.1</td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td id='cbreak' colspan=3 align="center">Coffee Break</td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td id='t01' rowspan=3 height="80" align="center" >11:00 - 12:00</td>
		<td id='clong_v' align="center" rowspan=3 >Poster 1.1</td>
		<td id='clong_v' align="center" rowspan=3 >Poster 2.1</td>
		<td id='clong_v' align="center" rowspan=3 >Poster 3.1</td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td id='t01' rowspan=3 height="99" align="center" >12:00 - 13:00</td>
		<td align="left" valign=bottom><br></td>
		<td id='cbreak'  align="center">Sponsor event / Lunch </td>
		<td id='cbreak' align="center">Sponsor event / Lunch </td>
		<td id='cbreak' align="center">Sponsor event / Lunch </td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><br></td>
		<td colspan=3 rowspan=3 id='cbreak' align="center" >Lunch</td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><br></td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td id='t01' rowspan=3 height="80" align="center" >13:00 - 14:00</td>
		<td align="left" valign=bottom><br></td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><br></td>
		<td id='cmentor' align="center" rowspan=2 >Oral 1.2</td>
		<td id='cmentor' align="center" rowspan=2 >Oral 2.2</td>
		<td id='cmentor' align="center" rowspan=2 >Oral 3.2</td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=bottom><br></td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td id='t01' rowspan=3 height="80" align="center" >14:00 - 15:00</td>
		<td rowspan=9 align="center" id='cposter'><a href='tutorials.html'>Tutorial II</a></td>
		<td id='cshort_v' align="center" rowspan=3 >Keynote 1</td>
		<td id='cshort_v' align="center" rowspan=3 >Keynote 2</td>
		<td id='cshort_v' align="center" rowspan=3 >Keynote 3</td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=top><br></td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=top><br></td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td id='t01' rowspan=3 height="80" align="center" >15:00 - 16:00</td>
		<td align="left" valign=top><br></td>
		<td id='cbreak'align="center" colspan=3 >Coffee Break</td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=top><br></td>
		<td id='clong_v' align="center" >Poster 1.2</td>
		<td id='clong_v' align="center" >Poster 2.2</td>
		<td id='clong_v' align="center" >Poster 2.3</td>
		<td align="left" valign=top><br></td>
	</tr>
	<tr>
		<td align="left" valign=top><br></td>
		<td align="left" valign=top><br></td>
		<td align="left" valign=top><br></td>
		<td align="left" valign=top><br></td>
		<td align="left" valign=top><br></td>
	</tr>
</table>