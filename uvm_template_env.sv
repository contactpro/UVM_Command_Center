// 
// Author:  
// Filename: uvm_template_env.sv  
// Version: Demo   
// Description: env template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries 
//
`ifndef PKT_ENV_SV
`define PKT_ENV_SV

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/packet_seq_item.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_sequence.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_agent.sv"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/uvm_template_scoreboard.sv"

class uvm_template_env extends uvm_env;
  int num_seqs = 4;
  
  `uvm_component_utils_begin(uvm_template_env)
      `uvm_field_int(num_seqs, UVM_ALL_ON)
  `uvm_component_utils_end
  
  // constructor 
  function new (string name = "uvm_template_env", uvm_component parent=null);
    super.new(name, parent);
  endfunction: new
     
  uvm_template_agent agnt;
  
  uvm_template_scoreboard scbd;
  
  // virtual interface
  virtual my_if vif;  
  
  // phase progress information funtion
  function void phase_started(uvm_phase phase);
    `uvm_info("PHASE_STATUS", $sformatf("Phase started for %s", phase.get_name()), UVM_NONE);
  endfunction: phase_started
  
  // build phase 
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);   
    `uvm_info(get_type_name(),"In ENV BUILD PHASE . . .", UVM_MEDIUM);
    uvm_config_db#(virtual my_if)::get(this, "", "vif", vif);     
    agnt = uvm_template_agent::type_id::create("agnt", this);
    scbd = uvm_template_scoreboard::type_id::create("scbd", this);      
  endfunction: build_phase
  
  // connect phase
  virtual function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
    // connect the scoreboard with the agent
    agnt.mon.item_collected_port.connect(scbd.ap_imp);
  endfunction: connect_phase  

  // run phase  
  virtual task run_phase (uvm_phase phase);
    // uvm_template_sequence m_seq;
    // m_seq = uvm_template_sequence::type_id::create("m_seq");
    super.run_phase(phase);
    // phase.raise_objection(this);
    //       m_seq.start(uvm_test_top.env.agnt.seqr);
    //       m_seq.start(uvm_template_base_test.env.agnt.seqr);
    // -------------------------------------------------------
    // Simulation Error: env.sv(66): 
    // Actual input arg. of type 'reg' for formal 'sequencer' 
    // of 'start' is not compatible with the formal's type 
    // 'class work.uvm_pkg::uvm_sequencer_base'.
    // replaced with sequencer start in test class
    //
    // m_seq.start(env.agnt.seqr);
    // phase.drop_objection(this);
  endtask: run_phase
    
endclass: uvm_template_env

`endif


