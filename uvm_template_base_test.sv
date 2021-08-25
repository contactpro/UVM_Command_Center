// 
// Author:  
// Filename: uvm_template_base_test.sv  
// Version: Demo   
// Description: base_test template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//
`ifndef PKT_BASE_TEST
`define PKT_BASE_TEST

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/packet_seq_item.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_env.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_sequence.sv"

class uvm_template_base_test extends uvm_test;
  `uvm_component_utils(uvm_template_base_test)

  // constructor
  function new(string name = "uvm_template_base_test", uvm_component parent=null);
    super.new(name, parent);
  endfunction: new

  // env instance  
  uvm_template_env env;

  // build_phase
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
      `uvm_info(get_type_name(),"In BUILD PHASE . . .", UVM_MEDIUM);  
      // Create the env
      env = uvm_template_env::type_id::create("env", this);
      
  endfunction: build_phase
  
  // connect phase
  virtual function void connect_phase(uvm_phase phase);
  endfunction: connect_phase  
  
  // end_of_elaboration_phase 
  virtual function void end_of_elaboration_phase(uvm_phase phase);
    // print the topology
    uvm_top.print_topology();
  endfunction: end_of_elaboration_phase

  // run phase
  virtual task run_phase (uvm_phase phase);
  endtask: run_phase

  // report phase
  function void report_phase(uvm_phase phase);
    uvm_report_server svr;
    super.report_phase(phase);
   
    svr = uvm_report_server::get_server();
    if(svr.get_severity_count(UVM_FATAL)+svr.get_severity_count(UVM_ERROR)>0) begin
      `uvm_info(get_type_name(), "---------------------------------------", UVM_NONE)
      `uvm_info(get_type_name(), "----            TEST FAIL          ----", UVM_NONE)
      `uvm_info(get_type_name(), "---------------------------------------", UVM_NONE)
    end
    else begin
     `uvm_info(get_type_name(), "---------------------------------------", UVM_NONE)
     `uvm_info(get_type_name(), "----           TEST PASS           ----", UVM_NONE)
     `uvm_info(get_type_name(), "---------------------------------------", UVM_NONE)
    end
  endfunction: report_phase 
  
endclass: uvm_template_base_test

`endif
