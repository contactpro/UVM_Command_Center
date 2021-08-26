 // 
// Author: 
// Filename: my_uvm_report_server.sv  
// Version: Demo       
// Description: my_uvm_report_server template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//  
// Define your custom format for the report server. 
class my_uvm_report_server extends uvm_report_server;
  `uvm_object_utils(my_uvm_report_server)
     
  // constructor   
  function new(string name="my_uvm_report_server", uvm_object parent=null);
    super.new(name, parent);
  endfunction: new

  virtual function string compose_message( uvm_severity severity,
                                        string name,
                                        string id,
                                        string message,
                                        string filename,
                                        int line );                                        
  uvm_severity_type severity_type = uvm_severity_type'( severity );
  return $psprintf( "%-8s | %16s | %2d | %0t | %-21s | %-7s | %s",
     severity_type.name(), filename, line, $time, name, id, message );
  endfunction: compose_message
   
endclass: my_uvm_report_server
