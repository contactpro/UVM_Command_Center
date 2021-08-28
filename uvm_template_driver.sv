// 
// Author: 
// Filename: uvm_template_driver.sv  
// Version: Demo       
// Description: driver template for UVM Testbench Builder
// Language: SystemVerilog and UVM Libraries
//
`ifndef PKT_DRIVER_SV
`define PKT_DRIVER_SV

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/packet_seq_item.sv"

class uvm_template_driver extends uvm_driver #(packet_seq_item);
  `uvm_component_utils(uvm_template_driver)
  
  // virtual interface
  virtual my_if vif;
  
  // constructor
  function new (string name="uvm_template_driver", uvm_component parent=null);
    super.new(name, parent);
  endfunction : new

  // phase progress information funtion
  function void phase_started(uvm_phase phase);
    `uvm_info("PHASE_STATUS", $sformatf("Phase started for %s", phase.get_name()), UVM_NONE);
  endfunction: phase_started

  // build phase
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
      `uvm_info(get_type_name(),"In BUILD PHASE . . .", UVM_MEDIUM);
      uvm_config_db#(virtual my_if)::get(this, "", "vif", vif);
  endfunction: build_phase

  // run phase
  virtual task run_phase(uvm_phase phase);
      packet_seq_item pkt;
      packet_seq_item pkt_rsp;
      forever begin
        pkt = packet_seq_item::type_id::create("Our Packet");
        pkt_rsp = packet_seq_item::type_id::create("Our Packet Response");     	
    	  @(posedge vif.clk); 
        seq_item_port.get_next_item(pkt);
        drive(); // drive_item(req, rsp);
        pkt_rsp.set_id_info(pkt); // assign the pkt transaction id to corresponding rsp
        seq_item_port.item_done(pkt_rsp); // send rsp transaction as feedback
        `uvm_info("UVM_TEMPLATE_DRIVER",{"PKT REQ Transaction Completed:\n", pkt.sprint()}, UVM_MEDIUM);
        `uvm_info("UVM_TEMPLATE_DRIVER",{"PKT RSP Transaction Completed:\n", pkt_rsp.sprint()}, UVM_MEDIUM);
      end
  endtask: run_phase
  
  //----------------------------------------------------------------
  // drive task - drive transaction level to signal level
  // drives the value's from packet_seq_item to interface signals
  //----------------------------------------------------------------
  virtual task drive();
    vif.wr_en <= 0;
    vif.rd_en <= 0;
    @(posedge vif.clk); 
    
    vif.addr <= req.addr;
    
    if(req.wr_en) begin // write operation
      vif.wr_en <= req.wr_en;
      vif.wdata <= req.wdata;
      @(posedge vif.clk);
    end
    else if(req.rd_en) begin // read operation
      vif.rd_en <= req.rd_en;
      @(posedge vif.clk);
      vif.rd_en <= 0;
      @(posedge vif.clk);
      req.rdata = vif.rdata;
      @(posedge vif.clk);
    end
    
  endtask : drive
  
endclass : uvm_template_driver

`endif

