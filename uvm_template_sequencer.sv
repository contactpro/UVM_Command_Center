// 
// Author:  
// Filename: uvm_template_sequencer.sv  
// Version: Demo   
// Description: sequencer template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries 
//
`ifndef PKT_SEQUENCER_SV
`define PKT_SEQUENCER_SV

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/packet_seq_item.sv"

class uvm_template_sequencer extends uvm_sequencer #(packet_seq_item);
  `uvm_component_utils(uvm_template_sequencer) 
 
  //constructor
  function new(string name = "uvm_template_sequencer", uvm_component parent=null);
    super.new(name,parent);
  endfunction

  // phase progress information funtion
  function void phase_started(uvm_phase phase);
    `uvm_info("PHASE_STATUS", $sformatf("Phase started for %s", phase.get_name()), UVM_NONE);
  endfunction: phase_started
  
  // build phase
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
      `uvm_info("SEQUENCER","In SEQUENCER BUILD PHASE . . .", UVM_MEDIUM);
  endfunction: build_phase 
   
  // run phase
  virtual task run_phase(uvm_phase phase);
  endtask: run_phase
  
endclass: uvm_template_sequencer

`endif

