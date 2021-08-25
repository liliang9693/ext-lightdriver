
//% color="#d3a065" iconWidth=50 iconHeight=40
namespace lightdriver{
  
    //% block="driver init port[PORT] baudrate[BAUD]" blockType="command"
    //% PORT.shadow="string" PORT.defl="COM15"
    //% BAUD.shadow="number" BAUD.defl=9600
    export function init(parameter: any, block: any) {
        let port=parameter.PORT.code;
        let baud=parameter.BAUD.code;

        Generator.addImport(`from dri0050lib import DRI0050`);
        
        Generator.addCode(`ld=DRI0050(port=${port},baudrate=${baud})`);


    }         
    
    //% block="driver get[SHD]" blockType="command"
    //% SHD.shadow="dropdown" SHD.options="SHD"
    export function get(parameter: any, block: any) {
        let shd=parameter.SHD.code;

        Generator.addCode(`ld.${shd}`);


    }

    //% block="driver set freq[FREQ]" blockType="command"
    //% FREQ.shadow="range" FREQ.params.min=0    FREQ.params.max=10     FREQ.defl=860
    export function setfreq(parameter: any, block: any) {
        let freq=parameter.FREQ.code;

        Generator.addCode(`ld.set_freq(${freq})`);


    }    

    //% block="driver set duty[DUTY]" blockType="command"
    //% DUTY.shadow="range"  DUTY.params.min=0    DUTY.params.max=1     DUTY.defl=0.82
    export function setduty(parameter: any, block: any) {
        let duty=parameter.DUTY.code;


        Generator.addCode(`ld.set_duty(${duty})`);


    }    

    
    //% block="driver set enable[ENAB]" blockType="command"
    //% ENAB.shadow="dropdownRound"   ENAB.options="ENAB"     
    export function setenab(parameter: any, block: any) {
        let enab=parameter.ENAB.code;
        
        Generator.addCode(`ld.set_enable(${enab})`);


    }    



}
