import hashlib
import json
import re
import os
#获取两个加密参数
def string_to_hash(query, variables):
    combined_string = query + variables
    cleaned_string = re.sub(r'\W', '', combined_string)
    return cleaned_string
# 计算字符串 "Hello, world!" 的 SHA-256 哈希值
query='queryProductQuery($productId:String!){product(id:$productId){bopisEligiblecategories{namekey}clearancePromoMessagefinalsalePromoMessagecollectioncrossRelDetailMessagecrossRelProductURLEFOProductexpressProductTypefabricCarefabricDetailImages{captionimage}genderinternationalShippingAvailablelistPricemarketPlaceProductnamenewProductonlineExclusiveonlineExclusivePromoMsgpdpCrossSellHeaderproductDescription{typecontent}matchingSet{colorskus}productDetailproductFeaturesproductIdproductImageproductInventoryproductURLpromoMessagerecsAlgorithmoriginRecsAlgorithmsalePricetypebreadCrumbSummarybreadCrumbCategory{categoryNameh1CategoryNamelinks{relhref}breadCrumbCategory{categoryNameh1CategoryNamelinks{relhref}}}colorSlices{colorcolorFamilydefaultSliceipColorCodehasWaistAndInseamswatchURLimageMap{All{LARGEMAIN}Default{LARGEMAIN}Model1{LARGEMAIN}Model2{LARGEMAIN}Model3{LARGEMAIN}}mediaMap{main{urlsequenceId}large{urlsequenceId}modelInfo{sequenceIdlabelText}}onlineSkusskus{backOrderablebackOrderDatecategoryTypedisplayMSRPdisplayPriceextinseaminStoreInventoryCountinventoryMessageisFinalSaleisInStockOnlinemiraklOffer{minimumShippingPricesellerIdsellerName}marketPlaceSkuonClearanceonSaleonlineExclusiveonlineInventoryCountsizesizeNameskuId}}originRecs{listPricemarketPlaceProductnameproductIdproductImageproductURLsalePrice}relatedProducts{listPricemarketPlaceProductnameproductIdproductImageproductURLsalePricecolorSlices{colordefaultSlice}}storeTiericons{iconcategory}}}'
variables=json.dumps("{productId: '06747392'}")
# data=query+variables
data=string_to_hash(query,variables)
sha256 = hashlib.sha256()
sha256.update(data.encode('utf-8'))
digest = sha256.hexdigest()

result = os.popen('node ./requestid.js').read()
print(result)
print(digest)



# cmd = 'node -e "require(\'%s\').init()"' % './requestid'
# pipeline=os.popen(cmd)
# result=pipeline.read()
# print(result)