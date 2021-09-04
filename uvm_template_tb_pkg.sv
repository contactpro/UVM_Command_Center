// 
// Author:  
// Filename: uvm_template_tb_pkg.sv  
// Version: Demo   
// Description: tb_pkg template for UVM Testbench Builder. 
// This uvm_template_tb_pkg may be implemented
// in future releases as we add VARIABLES in the uvm testbench builder
// to allow specification of uvm library installation path
// and project paths that precede each uvm testbench filename.
// Language: SystemVerilog and UVM Libraries
//
`ifndef TB_PKG_SV
`define TB_PKG_SV

// Import the UVM library 
import uvm_pkg::*;

package uvm_template_tb_pkg;

// Include the UVM macros
`include "C:/Users/HP/WORK_UVM/uvm-1.1d/src/uvm_macros.svh"

`include "packet_seq_item.sv"

`include "uvm_template_interface.sv"

`include "uvm_template_sequence.sv"

`include "uvm_template_sequencer.sv"

`include "uvm_template_monitor.sv"
`include "uvm_template_driver.sv"
`include "uvm_template_agent.sv"
`include "uvm_template_scoreboard.sv"
`include "uvm_template_env.sv"

`include "uvm_template_base_test.sv"
// `include "other_name_test.sv"

endpackage