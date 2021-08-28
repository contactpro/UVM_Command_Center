// 
// Author:  
// Filename: uvm_template_agent.sv  
// Version: Demo   
// Description: agent template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//

`ifndef PKT_AGENT_SV
`define PKT_AGENT_SV

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/packet_seq_item.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_sequencer.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_driver.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_monitor.sv"

class uvm_template_agent extends uvm_agent;
  `uvm_component_utils(uvm_template_agent)
  
  uvm_template_sequencer seqr;
  uvm_template_driver drv;
  uvm_template_monitor mon;
  uvm_template_monitor mon_dut_out;
  
  // constructor
  function new (string name = "uvm_template_agent", uvm_component parent=null);
    super.new(name, parent);
  endfunction
  
  // phase progress information funtion
  function void phase_started(uvm_phase phase);
    `uvm_info("PHASE_STATUS", $sformatf("Phase started for %s", phase.get_name()), UVM_NONE);
  endfunction: phase_started
  
  // build phase
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
    `uvm_info("AGENT_BUILD_PHASE","In AGENT BUILD PHASE . . .", UVM_MEDIUM);
    
    if(get_is_active() == UVM_ACTIVE) begin
      drv = uvm_template_driver::type_id::create("drv", this);
      seqr = uvm_template_sequencer::type_id::create("seqr", this);
    end

    mon = uvm_template_monitor::type_id::create("mon", this);  
     
  endfunction: build_phase
  
  // list the things that are connected in this agent class
  // versus any connections in the env class
  // connect phase 
  function void connect_phase(uvm_phase phase);
    if(get_is_active() == UVM_ACTIVE) begin
      drv.seq_item_port.connect(seqr.seq_item_export);
    end
 
  endfunction: connect_phase
   
  // run phase
  virtual task run_phase(uvm_phase phase);
  endtask: run_phase
  
endclass: uvm_template_agent

`endif

