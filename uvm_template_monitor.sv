// 
// Author:  
// Filename: uvm_template_monitor.sv  
// Version: Demo   
// Description: monitor template for UVM Testbench Builder 
// Language: SystemVerilog and UVM Libraries
//
`ifndef PKT_MONITOR_SV
`define PKT_MONITOR_SV

import uvm_pkg::*;
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"

`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/BUILD_TEST/UVM_COMMAND_CENTER_v1.8/packet_seq_item.sv"

class uvm_template_monitor extends uvm_monitor;
  
  int packet_count = 0;
  
  // virtual interface
  virtual my_if vif;
  
  packet_seq_item pkt;

  uvm_analysis_port#(packet_seq_item) item_collected_port;
   
  // factory 
  `uvm_component_utils_begin(uvm_template_monitor)
      `uvm_field_int(packet_count, UVM_ALL_ON)
  `uvm_component_utils_end
  
  // constructor
  function new (string name="uvm_template_monitor", uvm_component parent=null);
    super.new(name, parent);
  endfunction : new

  // phase progress information funtion
  function void phase_started(uvm_phase phase);
    `uvm_info("MONITOR_PHASE_STATUS", $sformatf("Phase started for %s", phase.get_name()), UVM_NONE);
  endfunction: phase_started

  // build phase
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
      `uvm_info("MONITOR_BUILD_PHASE","In MONITOR BUILD PHASE . . .", UVM_MEDIUM);
      uvm_config_db#(virtual my_if)::get(this, "", "vif", vif);  
  endfunction: build_phase
  
  task main_phase(uvm_phase phase);
     fork
     	  collect_transaction();
     join_none
  endtask
   
  // collect transaction task in monitor class
  task collect_transaction();
     pkt = packet_seq_item::type_id::create("Our Packet");
     forever @(negedge vif.clk) begin
        if (vif.rd_en=='1) begin
      	   void'(this.begin_tr(pkt));
      	   pkt.rdata = vif.rdata;
      	   pkt.wdata = vif.wdata;
      	   pkt.rd_en = vif.rd_en;
      	   pkt.wr_en = vif.wr_en;
      	   pkt.addr  = vif.addr;
      	   //pkt.last_item = 0;
           `uvm_info("UVM_TEMPLATE_MONITOR",{"Monitor Collected Transaction:\n", pkt.sprint()}, UVM_MEDIUM);
           ++packet_count;
           `uvm_info("UVM_TEMPLATE_MONITOR_PACKET_COUNT",$sformatf("packet_count: %0d", packet_count), UVM_MEDIUM);
           // WRITE PACKET TO MONITOR ANALYSIS PORT
           item_collected_port.write(pkt); 
           @(posedge vif.clk) void'(this.end_tr(pkt));
        end // if
    end // forever
  endtask : collect_transaction
  
  function void report_phase(uvm_phase phase);
      super.report_phase(phase);
      `uvm_info("UVM_MONITOR_REPORT_PHASE", "Completed Monitoring Packets. ", UVM_LOW);  
  endfunction: report_phase
  
endclass : uvm_template_monitor

`endif


