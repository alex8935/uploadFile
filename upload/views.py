from django.shortcuts import render

# Create your views here.

import requests

def request(request):
        url = 'http://api.sellercloud.com/BulkUpdateFieldsQueueSmart'
        userName = ''
        password = ''

        headers = {{'POST /scservice.asmx HTTP/1.1'},
        {'Host': 'ws.rocksignal.com'},
        {'Content-Type': 'application/soap+xml; charset=utf-8'},
        {'Content-Length': 'length'}}
        body = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Header>
    <AuthHeader xmlns="http://api.sellercloud.com/">
      <ApplicationName>string</ApplicationName>
      <ApplicationVersion>string</ApplicationVersion>
      <UserName>string</UserName>
      <Password>string</Password>
    </AuthHeader>
    <ServiceOptions xmlns="http://api.sellercloud.com/">
      <AlwaysRecalculateWeight>boolean</AlwaysRecalculateWeight>
      <CalculateWeightIgnoreZeroWeightProducts>boolean</CalculateWeightIgnoreZeroWeightProducts>
      <AllowAnyProductShippingMethods>boolean</AllowAnyProductShippingMethods>
      <FetchUserDefinedColumnsForProducts>boolean</FetchUserDefinedColumnsForProducts>
      <SkipBundleItemQtyUpdating>boolean</SkipBundleItemQtyUpdating>
      <DoNotGetClientUser>boolean</DoNotGetClientUser>
      <SkipCWAShippingRules>boolean</SkipCWAShippingRules>
      <DontIncludePORMAImages>boolean</DontIncludePORMAImages>
      <IncludeClientUserAddressBook>boolean</IncludeClientUserAddressBook>
      <SaveOrderPackageDimensions>boolean</SaveOrderPackageDimensions>
      <CreateNewProducts>boolean</CreateNewProducts>
      <SplitItems>boolean</SplitItems>
      <PaymentNotNeeded>boolean</PaymentNotNeeded>
      <DebugInfo>string</DebugInfo>
      <DoNotDownloadImageData>boolean</DoNotDownloadImageData>
      <BulkWipeRelationships>boolean</BulkWipeRelationships>
      <BulkDeleteShadows>boolean</BulkDeleteShadows>
      <BulkResetOffsetQty>boolean</BulkResetOffsetQty>
      <UseCache>boolean</UseCache>
      <DontNeedCompanyProfile>boolean</DontNeedCompanyProfile>
    </ServiceOptions>
  </soap12:Header>
  <soap12:Body>
    <BulkUpdateFieldsQueueSmart xmlns="http://api.sellercloud.com/">
      <contents>string</contents>
      <isUPCFirst>boolean</isUPCFirst>
      <subtractUnExportedOrderInventoryQty>boolean</subtractUnExportedOrderInventoryQty>
      <CreateNewProducts>boolean</CreateNewProducts>
      <subtractUnshippedOrderInventoryQty>boolean</subtractUnshippedOrderInventoryQty>
      <options>
        <OriginalFileName>string</OriginalFileName>
        <OnlyUpdateProductsForCompany>int</OnlyUpdateProductsForCompany>
        <CustomCompanyID>int</CustomCompanyID>
        <CompanyIDForNewProducts>int</CompanyIDForNewProducts>
        <UsePlugin>boolean</UsePlugin>
        <PluginName>string</PluginName>
      </options>
    </BulkUpdateFieldsQueueSmart>
  </soap12:Body>
</soap12:Envelope>"""

        response = requests.post(url, data=body, headers=headers)
        return response.content