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

  function string getShortFileName(string s);
     int offset = 0;
     int lastChar;
     string shortFileName;
     int slashPosition;
      
     lastChar = s.len()-1;
     for (int i = lastChar; i >= offset; i=i-1) begin
       if (s.getc(i) inside {"/", "\\"}) begin
         slashPosition = i;
         break;
       end
     end // for loop
          
     shortFileName = s.substr(slashPosition+1, lastChar);
     return shortFileName;
  endfunction

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
       // Note that the id is going to be the 32 character MESSAGE ID that 
       // encodes or represents a MESSAGE ID which is used as a SIGNATURE
       // to categorize testbench info, errors, fatal errors, warning messages.
       // These 32 character SIGNATURES can be utilized to organize and identify
       // testbench results by UVM MESSAGE ID SIGNATURE. 
       string id_fixed_length_string = "12345678901234567890123456789012";
       string id_fixed_length_default_string = "ID_32CHAR_TEST_RESULTS_SIGNATURE";
       int    id_desired_length = 32; // set the desired length of the id to 32
       int    id_actual_length;
   
       sv = uvm_severity_type'(severity);
       $swrite(time_str, "%0t", $realtime); 
       
       id_actual_length = id.len();
      
       if (id_actual_length > 32) begin
       	 `uvm_error("REPORT_SERVER_ID_STRING_LENGTH_ERROR","REPORT SERVER ID STRING TOO LONG ERROR !!")
       end       
       
       foreach (id_fixed_length_string[k]) begin
         id_fixed_length_string[k] = "_";
       end
       
       foreach (id[i]) begin
       	 id_fixed_length_string[i] = id[i];
       end  
             	 
       case(1)
       	 (name == "" && filename == ""):
       	          return $psprintf( "@%7tns | %-8s [%32s] %16s [%2d] %-21s | %s", $time, sv.name(), id_fixed_length_string, filename, line, name, message);
         (name != "" && filename == ""):
       	          return $psprintf( "@%7tns | %-8s [%32s] %16s [%2d] %-21s | %s", $time, sv.name(), id_fixed_length_string, filename, line, name, message);
       	 (name == "" && filename != ""):
       	      begin
       	      	  return $psprintf( "@%7tns | %-8s [%32s] %16s [%2d] %-21s | %s", $time, sv.name(), id_fixed_length_string, getShortFileName(filename), line, name, message);
       	      end
       	 (name != "" && filename != ""):
       	      begin
       	      	  return $psprintf( "@%7tns | %-8s [%32s] %16s [%2d] %-21s | %s", $time, sv.name(), id_fixed_length_string, getShortFileName(filename), line, name, message);
       	      end       	      	  
       endcase    	                 
  endfunction: compose_message
   
endclass: my_uvm_report_server


`endif
