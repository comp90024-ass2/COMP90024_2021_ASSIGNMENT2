function (doc) {
  emit([doc.user_location,doc.lang_detected], doc.happines);
}
