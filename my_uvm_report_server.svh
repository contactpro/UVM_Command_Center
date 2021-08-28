 // 
// Author: 
// Filename: my_uvm_report_server.sv  
// Version: Demo       
// Description: my_uvm_report_server template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//  
// Define your custom format for the report server. 

`ifndef CUSTOM_REPORT_SERVER
`define CUSTOM_REPORT_SERVER

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"

class my_uvm_report_server extends uvm_report_server;
  // `uvm_component_utils(my_uvm_report_server)
  
  uvm_report_server old_report_server;
  uvm_report_global_server global_server;
 
 // constructor 
  function new(string name="my_uvm_report_server");
    super.new(); 
    set_name(name);
    global_server = new();
    old_report_server = global_server.get_server();
    global_server.set_server(this);
    `uvm_info("MY_UVM_REPORT_SERVER","END CUSTOM REPORT SERVER Constructor . . .",UVM_MEDIUM)
  endfunction: new

  virtual function string compose_message(
         uvm_severity severity,
         string name,
         string id,
         string message,
         string filename,
         int    line
         );
       uvm_severity_type sv;
       string time_str;
       string line_str;
                         
       sv = uvm_severity_type'(severity);
       $swrite(time_str, "%0t", $realtime);
       
       case(1)
       	 (name == "" && filename == ""):
       	          // return {sv.name(), " @ ", time_str, " [", id, "] ", message};
       	          return $psprintf( "%-8s | %16s | %2d | %0t | %-21s | %-7s | %s", sv.name(), filename, line, $time, name, id, message );
         (name != "" && filename == ""):
       	          // return {sv.name(), " @ ", time_str, ": ", name, " [", id, "] ", message};
       	          return $psprintf( "%-8s | %16s | %2d | %0t | %-21s | %-7s | %s", sv.name(), filename, line, $time, name, id, message );
       	 (name == "" && filename != ""):
       	      begin
       	      	  // $swrite(line_str, "%0d", line); 
       	      	  // return {sv.name(), " ", filename, "(", line_str, ")", " @ ", time_str, " [", id, "] ", message};
       	      	  return $psprintf( "%-8s | %16s | %2d | %0t | %-21s | %-7s | %s", sv.name(), filename, line, $time, name, id, message );
       	      end
       	 (name != "" && filename != ""):
       	      begin
       	      	  // $swrite(line_str, "%0d", line);
       	      	  // return {sv.name(), " ", filename, "(", line_str, ")", " @ ", time_str, ": ", name," [", id, "] ", message};
       	      	  return $psprintf( "%-8s | %16s | %2d | %0t | %-21s | %-7s | %s", sv.name(), filename, line, $time, name, id, message );
       	      end       	      	  
       endcase    	                 
       // return $psprintf( "%-8s | %16s | %2d | %0t | %-21s | %-7s | %s", sv.name(), filename, line, $time, name, id, message );
       // return $psprintf( "%-8s | %16s | %2d | %0t | %-21s | %-7s | %s", sv.name(), filename, line, $time, name, id, message );
  endfunction: compose_message
   
endclass: my_uvm_report_server


`endif
