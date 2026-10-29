package com.mssumy.gsmpro

import android.content.Context
import android.hardware.usb.UsbDevice
import android.hardware.usb.UsbManager
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    private lateinit var usbManager: UsbManager
    private lateinit var statusText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        usbManager = getSystemService(Context.USB_SERVICE) as UsbManager
        statusText = findViewById(R.id.statusText)

        val btnScan = findViewById<Button>(R.id.btnScan)
        btnScan.setOnClickListener {
            scanConnectedDevices()
        }
    }

    private fun scanConnectedDevices() {
        val deviceList: HashMap<String, UsbDevice> = usbManager.deviceList
        if (deviceList.isEmpty()) {
            statusText.text = "[!] Hakuna kifaa kilichochomekwa kupitia OTG!"
            return
        }

        var info = "[✓] Vifaa Vya OTG vimetambuliwa:\n"
        for (device in deviceList.values) {
            info += "-> Device: ${device.deviceName}\n"
            info += "-> Vendor ID: ${device.vendorId} | Product ID: ${device.productId}\n"
            info += "-> Manufacturer: ${device.manufacturerName ?: \"Unknown\"}\n"
        }
        statusText.text = info
    }
}
