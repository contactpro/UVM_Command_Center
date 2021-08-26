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
`include "C:/Users/HP/WORK_PYTHON/PY_UVM_TB_BUILDER/uvm_templates/packet_seq_item.sv"

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

  // build phase
  function void build_phase(uvm_phase phase);
    super.build_phase(phase);
      `uvm_info(get_type_name(),"In BUILD PHASE . . .", UVM_MEDIUM);
      pkt = packet_seq_item::type_id::create("Our Packet");
      uvm_config_db#(virtual my_if)::get(this, "", "vif", vif);
      item_collected_port = new("Monitor Port", this);      
  endfunction: build_phase
  
  // connect phase
  virtual function void connect_phase(uvm_phase phase);
    super.connect_phase(phase);
  endfunction: connect_phase    
  
  // run phase
  virtual task run_phase(uvm_phase phase);
    forever begin
      @(negedge vif.clk);
        if (vif.rd_en=='1) begin
      	  void'(this.begin_tr(pkt));
      	  pkt.rdata = vif.rdata;
      	  //pkt.last_item = 0;
          `uvm_info("UVM_TEMPLATE_MONITOR",{"Monitor Collected Transaction:\n", pkt.sprint()}, UVM_MEDIUM);
          ++packet_count;
          `uvm_info("UVM_TEMPLATE_MONITOR_PACKET_COUNT",$sformatf("packet_count: %0d", packet_count), UVM_MEDIUM);
          item_collected_port.write(pkt);
          @(posedge vif.clk) void'(this.end_tr(pkt));
        end // if
    end // forever
  endtask : run_phase
  
  function void report_phase(uvm_phase phase);
      super.report_phase(phase);
      `uvm_info("UVM_MONITOR_REPORT_PHASE", "Completed Monitoring Packets. ", UVM_LOW);  
  endfunction: report_phase
  
endclass : uvm_template_monitor

`endif


