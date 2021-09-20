// 
// Author:  
// Filename: uvm_template_wr_rd_test.sv  
// Version: Demo   
// Description: wr_rd_test template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//
`ifndef PKT_WR_RD_TEST
`define PKT_WR_RD_TEST

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"

`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.8/packet_seq_item.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.8/uvm_template_base_sequence.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.8/uvm_template_wr_rd_sequence.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.8/uvm_template_env.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.8/uvm_template_base_test.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.8/my_uvm_report_server.svh"

class uvm_template_wr_rd_test extends uvm_test;
  `uvm_component_utils(uvm_template_wr_rd_test)
  
  // custom report server instance 
  my_uvm_report_server report_server;
  
  // env instance  
  uvm_template_env env;
  
  // virtual interface
  virtual my_if vif;  
  
  uvm_cmdline_processor clp;
  
  // `uvm_component_utils(uvm_template_wr_rd_test)

  // constructor
  function new(string name = "uvm_template_wr_rd_test", uvm_component parent=null);
    super.new(name, parent);
    
    `uvm_info("WR_RD_TEST_CONSTRUCTOR_START","START OF WR_RD_TEST CONSTRUCTOR . . .", UVM_MEDIUM);

    uvm_config_db#(virtual my_if)::get(this, "", "vif", vif);
          
    clp = uvm_cmdline_processor::get_inst();

  endfunction: new
  
  // phase progress information funtion
  function void phase_started(uvm_phase phase);
    `uvm_info("WR_RD_TEST_PHASE_STATUS", $sformatf("Phase started for %s", phase.get_name()), UVM_NONE);
  endfunction: phase_started    
  
  // build_phase 
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    // Create the env
    env = uvm_template_env::type_id::create("env", this);          
      `uvm_info("WR_RD_TEST_BUILD_PHASE", "In WR_RD_TEST BUILD PHASE . . .", UVM_NONE);
                    
  endfunction: build_phase
  
   // end_of_elaboration_phase  
  function void end_of_elaboration_phase(uvm_phase phase);
     `uvm_info("WR_RD_TEST_ELAB_PRINT_TOPOLOGY", "Printing UVM Testbench Topology.", UVM_NONE); 
     // print the topology
     uvm_top.print_topology();
     factory.print();
     
     `uvm_info("WR_RD_TEST_ELABORATION_PHASE", "Setting report_server.", UVM_NONE);   
     report_server = new("report_server");
     uvm_report_server::set_server(report_server);
 	  	
  endfunction: end_of_elaboration_phase 
  
  // run phase - start the seq on the specified seqr 
  task run_phase(uvm_phase phase);
    uvm_template_wr_rd_sequence seq;
    seq = uvm_template_wr_rd_sequence::type_id::create("seq", this);
    phase.raise_objection(this);
    seq.start(env.agnt.seqr);
    `uvm_info("WR_RD_TEST_RUN_PHASE", "Created Sequence and Started Sequence on Sequencer.", UVM_NONE);     
    #1000;
    phase.drop_objection(this);
  endtask: run_phase   
 
  // report phase  
  function void report_phase(uvm_phase phase);

    uvm_report_server svr; 
            
    super.report_phase(phase);
    
    `uvm_info("WR_RD_TEST_REPORT_PHASE", "Getting report_server . . .", UVM_NONE);
     
    svr = uvm_report_server::get_server(); 
    
    if(svr.get_severity_count(UVM_FATAL)+svr.get_severity_count(UVM_ERROR)>0) begin
      `uvm_info("WR_RD_TEST_FAIL", "---------------------------------------", UVM_NONE)
      `uvm_info("WR_RD_TEST_FAIL", "----            TEST FAIL          ----", UVM_NONE)
      `uvm_info("WR_RD_TEST_FAIL", "---------------------------------------", UVM_NONE)
    end
    else begin
     `uvm_info("WR_RD_TEST_PASS", "---------------------------------------", UVM_NONE)
     `uvm_info("WR_RD_TEST_PASS", "----           TEST PASS           ----", UVM_NONE)
     `uvm_info("WR_RD_TEST_PASS", "---------------------------------------", UVM_NONE)
    end
  endfunction: report_phase 
  
endclass : uvm_template_wr_rd_test

`endif